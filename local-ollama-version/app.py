import streamlit as st
import os
from dotenv import load_dotenv
from agents import run_research
import json
from datetime import datetime
from fpdf import FPDF
from datetime import datetime

# 1. Load the secret key automatically
load_dotenv()

st.set_page_config(page_title="Agentic Deep Researcher", layout="wide")

# 2. Setup Session State for Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

if "research_history" not in st.session_state:
    st.session_state.research_history = []

# 3. Sidebar
with st.sidebar:
    st.header("⚙️ Configuration")
    api_status = "✅ Connected" if os.getenv("LINKUP_API_KEY") else "❌ Missing Key"
    st.info(f"LinkUp API Status: {api_status}")
    
    st.divider()
    st.subheader("📚 Research History")
    
    # Show all previous researches
    if st.session_state.research_history:
        for idx, research in enumerate(st.session_state.research_history, 1):
            with st.expander(f"🔍 Research #{idx}: {research['topic'][:40]}..."):
                st.write(f"**Topic:** {research['topic']}")
                st.write(f"**Time:** {research['timestamp']}")
                st.markdown(research['result'][:500] + "..." if len(research['result']) > 500 else research['result'])
                
                # Button to reload this research
                if st.button(f"Reload Research #{idx}", key=f"reload_{idx}"):
                    st.session_state.current_research = research['result']
                    st.rerun()
    else:
        st.write("No research history yet.")
    
    st.divider()
    
    if st.button("Clear All History 🗑️"):
        st.session_state.research_history = []
        st.session_state.messages = []
        st.rerun()

# 4. Main Header
st.title("🔍 Agentic Deep Researcher")
st.markdown("Powered by **DeepSeek-R1 (Local)** & **LinkUp (Web)** with Memory 💾")

# 5. Display Chat History
if st.session_state.messages:
    st.subheader("💬 Conversation History")
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    st.divider()

# 6. Chat Input & Processing
st.subheader("🚀 New Research Query")
if prompt := st.chat_input("What do you want to research?"):
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(f"**You:** {prompt}")

    # Check for API Key
    if not os.getenv("LINKUP_API_KEY"):
        st.error("❌ LinkUp API Key not found. Please add it to your .env file!")
        st.stop()

    # Run the Agents
    with st.chat_message("assistant"):
        # Show progress indicator
        progress_text = st.empty()
        progress_bar = st.progress(0)
        
        progress_text.text("🔍 Searching for papers...")
        progress_bar.progress(20)
        
        try:
            # Run research
            result = run_research(prompt)
            
            progress_bar.progress(100)
            progress_text.empty()
            progress_bar.empty()
            
            # Show final answer
            st.markdown(result)
            
            # Save to conversation history
            st.session_state.messages.append({
                "role": "assistant",
                "content": result
            })
            
            # Save to research history with timestamp
            st.session_state.research_history.append({
                "topic": prompt,
                "result": result,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
            
            st.success("✅ Research complete!")
            
        except Exception as e:
            progress_bar.empty()
            progress_text.empty()
            
            error_msg = f"An error occurred: {e}"
            st.error(error_msg)
            
            # Show detailed traceback
            with st.expander("🐛 Error Details"):
                st.exception(e)
            
            st.session_state.messages.append({
                "role": "assistant",
                "content": f"❌ {error_msg}"
            })

# 7. Optional: Save/Load Research Sessions
st.divider()
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("📥 Export Research as JSON"):
        if st.session_state.research_history:
            json_data = json.dumps(st.session_state.research_history, indent=2)
            st.download_button(
                label="Download JSON",
                data=json_data,
                file_name="research_history.json",
                mime="application/json"
            )
        else:
            st.warning("No research to export!")

with col2:
    if st.button("📄 Export as Markdown"):
        if st.session_state.research_history:
            markdown_content = "# Research History\n\n"
            for idx, research in enumerate(st.session_state.research_history, 1):
                markdown_content += f"## Research #{idx}\n"
                markdown_content += f"**Topic:** {research['topic']}\n\n"
                markdown_content += f"**Date:** {research['timestamp']}\n\n"
                markdown_content += f"{research['result']}\n\n"
                markdown_content += "---\n\n"
            
            st.download_button(
                label="Download Markdown",
                data=markdown_content,
                file_name="research_history.md",
                mime="text/markdown"
            )
        else:
            st.warning("No research to export!")
# Replace col3 section (around line 140) with this:
with col3:
    if st.button("📕 Export Latest as PDF"):
        if st.session_state.research_history:
            latest = st.session_state.research_history[-1]
            
            # Create simple PDF
            pdf = FPDF()
            pdf.add_page()
            
            # Title
            pdf.set_font("Arial", 'B', 16)
            pdf.cell(0, 10, "Research Report", ln=True, align='C')
            pdf.ln(5)
            
            # Topic
            pdf.set_font("Arial", 'B', 12)
            pdf.multi_cell(0, 10, f"Topic: {latest['topic']}")
            pdf.ln(3)
            
            # Timestamp
            pdf.set_font("Arial", 'I', 10)
            pdf.cell(0, 10, f"Generated: {latest['timestamp']}", ln=True)
            pdf.ln(5)
            
            # Content
            pdf.set_font("Arial", '', 11)
            # Clean text for PDF
            clean_text = latest['result'].encode('latin-1', 'replace').decode('latin-1')
            pdf.multi_cell(0, 7, clean_text)
            
            # Output
            pdf_output = pdf.output(dest='S').encode('latin-1')
            
            st.download_button(
                label="⬇️ Download PDF",
                data=pdf_output,
                file_name=f"research_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf",
                mime="application/pdf"
            )
        else:
            st.warning("No research to export!")