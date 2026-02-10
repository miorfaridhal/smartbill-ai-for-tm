import streamlit as st
import PyPDF2
import io
from datetime import datetime
try:
    from sample_data import get_sample_bill
    DEMO_AVAILABLE = True
except ImportError:
    DEMO_AVAILABLE = False

# Page configuration
st.set_page_config(
    page_title="SmartBill AI - TM Bill Analyzer",
    page_icon="📱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #E30613;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .info-box {
        background-color: #f0f8ff;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #2196F3;
        margin: 1rem 0;
    }
    .warning-box {
        background-color: #fff3cd;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #ffc107;
        margin: 1rem 0;
    }
    .success-box {
        background-color: #d4edda;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #28a745;
        margin: 1rem 0;
    }
    .stButton>button {
        background-color: #E30613;
        color: white;
        font-weight: bold;
        border-radius: 5px;
        padding: 0.5rem 2rem;
        border: none;
    }
    .stButton>button:hover {
        background-color: #c00510;
    }
    </style>
""", unsafe_allow_html=True)


def extract_text_from_pdf(pdf_file):
    """Extract text from uploaded PDF file"""
    try:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text
    except Exception as e:
        st.error(f"Error reading PDF: {str(e)}")
        return None


def parse_bill_info(bill_text):
    """Parse key information from bill text"""
    info = {
        'account_no': '',
        'bill_date': '',
        'total_amount': '',
        'due_date': '',
        'previous_balance': '',
        'current_charges': ''
    }
    
    # Simple parsing logic (can be enhanced)
    lines = bill_text.split('\n')
    for i, line in enumerate(lines):
        if 'Account No:' in line:
            info['account_no'] = line.split('Account No:')[-1].strip()
        elif 'Bill Date:' in line:
            info['bill_date'] = line.split('Bill Date:')[-1].strip()
        elif 'Total Amount Payable' in line and i + 1 < len(lines):
            # Look for RM amount in nearby lines
            for j in range(max(0, i-2), min(len(lines), i+3)):
                if 'RM' in lines[j]:
                    try:
                        amount = lines[j].split('RM')[-1].strip().split()[0]
                        info['total_amount'] = amount
                        break
                    except:
                        pass
        elif 'Pay before' in line:
            info['due_date'] = line.split('Pay before')[-1].strip().replace(')', '')
        elif 'Previous Balance' in line or 'Remaining balance from previous month' in line:
            if i + 1 < len(lines):
                for j in range(i, min(len(lines), i+3)):
                    if 'RM' in lines[j]:
                        try:
                            amount = lines[j].split('RM')[-1].strip().split()[0]
                            if amount and float(amount.replace(',', '')) > 0:
                                info['previous_balance'] = amount
                                break
                        except:
                            pass
    
    return info


def analyze_bill(bill_text):
    """Analyze the bill and generate insights"""
    info = parse_bill_info(bill_text)
    
    # Generate analysis sections
    analysis = {
        'summary': '',
        'breakdown': [],
        'changes': '',
        'recommendations': []
    }
    
    # Summary
    total = info.get('total_amount', 'N/A')
    due_date = info.get('due_date', 'N/A')
    analysis['summary'] = f"Your total bill is **RM {total}** and is due by **{due_date}**."
    
    # Check for previous balance
    prev_balance = info.get('previous_balance', '0')
    try:
        if prev_balance and float(prev_balance.replace(',', '')) > 0:
            analysis['summary'] += f"\n\n⚠️ **You have an outstanding balance of RM {prev_balance}** from the previous month that needs to be paid."
    except:
        pass
    
    # Breakdown
    if 'Monthly Charges' in bill_text or 'UNI5G' in bill_text or 'Postpaid' in bill_text:
        analysis['breakdown'].append("📱 **Monthly Plan Subscription** - Your regular monthly plan fee")
    
    if 'Service Tax' in bill_text:
        analysis['breakdown'].append("💰 **Service Tax (6%)** - Government tax on telecommunications services")
    
    if prev_balance and float(prev_balance.replace(',', '')) > 0:
        analysis['breakdown'].append(f"⏮️ **Previous Unpaid Balance** - RM {prev_balance} from last month")
    
    if 'Usage Charges' in bill_text:
        if 'Usage Charges 0.00' in bill_text or 'Usage Charges\n0.00' in bill_text:
            analysis['breakdown'].append("✅ **Usage Charges** - RM 0.00 (All calls/data covered by your plan)")
        else:
            analysis['breakdown'].append("📞 **Usage Charges** - Additional calls, SMS, or data beyond your plan")
    
    # Changes
    if prev_balance and float(prev_balance.replace(',', '')) > 0:
        analysis['changes'] = f"Your bill is higher than usual because of the **RM {prev_balance} unpaid balance** from last month. Your current month charges appear to be at the normal rate."
    else:
        analysis['changes'] = "Your bill appears stable compared to your regular monthly charges."
    
    # Recommendations
    if prev_balance and float(prev_balance.replace(',', '')) > 0:
        analysis['recommendations'].append(f"💡 **Clear your outstanding balance** of RM {prev_balance} to avoid service disruption")
    
    if due_date != 'N/A':
        analysis['recommendations'].append(f"⏰ **Pay before {due_date}** to avoid late fees and service disconnection")
    
    if 'Credit Limit' in bill_text:
        analysis['recommendations'].append("📊 **Monitor your credit limit** - You're approaching your account limit")
    
    analysis['recommendations'].append("✅ **Set up autopay** through the Unifi app to never miss a payment")
    analysis['recommendations'].append("📱 **Download the Unifi app** for easy bill management and payments")
    
    return analysis, info


# Main app layout
def main():
    # Header
    st.markdown('<div class="main-header">📱 SmartBill AI</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Your Intelligent TM Bill Analyzer</div>', unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.image("https://via.placeholder.com/200x80/E30613/FFFFFF?text=TM+unifi", use_container_width=True)
        st.markdown("---")
        st.markdown("### 📋 About SmartBill AI")
        st.markdown("""
        SmartBill AI helps you understand your Telekom Malaysia (TM) bills in simple, 
        clear language.
        
        **Features:**
        - 📄 Upload your PDF bill
        - 🔍 Get instant breakdown
        - 💡 Receive smart recommendations
        - ⚡ Quick payment reminders
        """)
        st.markdown("---")
        st.markdown("### 🔒 Privacy Notice")
        st.info("Your bill is processed locally and not stored on our servers.")
        
    # Main content
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### 📤 Upload Your TM Bill")
        st.markdown('<div class="info-box">Upload your TM bill PDF to get an instant, easy-to-understand analysis.</div>', unsafe_allow_html=True)
        
        uploaded_file = st.file_uploader(
            "Choose your TM bill PDF",
            type=['pdf'],
            help="Upload your monthly TM/Unifi bill in PDF format"
        )
        
        if uploaded_file is not None:
            st.success(f"✅ File uploaded: {uploaded_file.name}")
            
            # Show file details
            file_size = uploaded_file.size / 1024  # Convert to KB
            st.caption(f"File size: {file_size:.2f} KB")
            
            if st.button("🔍 Analyze Bill", use_container_width=True):
                with st.spinner("Analyzing your bill..."):
                    # Extract text from PDF
                    bill_text = extract_text_from_pdf(uploaded_file)
                    
                    if bill_text:
                        # Store in session state
                        st.session_state['bill_text'] = bill_text
                        st.session_state['analysis_done'] = True
                        st.rerun()
        
        # Demo mode button
        if DEMO_AVAILABLE:
            st.markdown("---")
            st.markdown("#### 🎯 Try Demo Mode")
            st.info("Don't have a bill? Try our demo with sample data!")
            if st.button("📋 Load Demo Bill", use_container_width=True):
                with st.spinner("Loading demo bill..."):
                    demo_bill = get_sample_bill()
                    st.session_state['bill_text'] = demo_bill
                    st.session_state['analysis_done'] = True
                    st.rerun()
    
    with col2:
        st.markdown("### ℹ️ How It Works")
        st.markdown("""
        1. **Upload** your TM bill PDF
        2. **Click** the Analyze Bill button
        3. **Get** instant breakdown and insights
        4. **Understand** your charges clearly
        """)
        
        st.markdown("### 💳 Accepted Bills")
        st.markdown("""
        - ✅ Unifi Mobile bills
        - ✅ Unifi Home bills
        - ✅ Unifi Air bills
        - ✅ Streamyx bills
        - ✅ All TM postpaid services
        """)
    
    # Display analysis if available
    if st.session_state.get('analysis_done', False) and st.session_state.get('bill_text'):
        st.markdown("---")
        st.markdown("## 📊 Your Bill Analysis")
        
        bill_text = st.session_state['bill_text']
        analysis, info = analyze_bill(bill_text)
        
        # Display bill info cards
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric(
                label="Account Number",
                value=info.get('account_no', 'N/A')
            )
        
        with col2:
            st.metric(
                label="Bill Date",
                value=info.get('bill_date', 'N/A')
            )
        
        with col3:
            st.metric(
                label="Total Amount",
                value=f"RM {info.get('total_amount', 'N/A')}"
            )
        
        with col4:
            st.metric(
                label="Due Date",
                value=info.get('due_date', 'N/A')
            )
        
        st.markdown("---")
        
        # Summary Section
        st.markdown("### 📝 Summary")
        st.markdown('<div class="success-box">' + analysis['summary'] + '</div>', unsafe_allow_html=True)
        
        # Breakdown Section
        st.markdown("### 💵 Charges Breakdown")
        for item in analysis['breakdown']:
            st.markdown(f"- {item}")
        
        # Changes Section
        st.markdown("### 📈 Why It Changed")
        st.markdown(analysis['changes'])
        
        # Recommendations Section
        st.markdown("### 💡 Things to Check & Recommendations")
        for rec in analysis['recommendations']:
            st.markdown(f"- {rec}")
        
        # Payment options
        st.markdown("---")
        st.markdown("### 💳 Quick Payment Options")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            **Online Banking**
            - JomPAY
            - Internet Banking
            - Mobile Banking
            """)
        
        with col2:
            st.markdown("""
            **E-Wallets**
            - Touch 'n Go
            - Boost
            - Shopee Pay
            """)
        
        with col3:
            st.markdown("""
            **Others**
            - Unifi App
            - 7-Eleven
            - 99 Speedmart
            """)
        
        # Reset button
        st.markdown("---")
        if st.button("🔄 Analyze Another Bill", use_container_width=True):
            st.session_state['analysis_done'] = False
            st.session_state['bill_text'] = None
            st.rerun()
        
        # Download option
        if st.button("📥 Download Analysis Report", use_container_width=True):
            # Create a text report
            report = f"""
SMARTBILL AI - BILL ANALYSIS REPORT
Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

ACCOUNT INFORMATION
Account Number: {info.get('account_no', 'N/A')}
Bill Date: {info.get('bill_date', 'N/A')}
Total Amount: RM {info.get('total_amount', 'N/A')}
Due Date: {info.get('due_date', 'N/A')}

SUMMARY
{analysis['summary']}

CHARGES BREAKDOWN
{chr(10).join('- ' + item for item in analysis['breakdown'])}

WHY IT CHANGED
{analysis['changes']}

RECOMMENDATIONS
{chr(10).join('- ' + rec for rec in analysis['recommendations'])}

---
Report generated by SmartBill AI
"""
            st.download_button(
                label="Download Text Report",
                data=report,
                file_name=f"bill_analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                mime="text/plain"
            )


if __name__ == "__main__":
    # Initialize session state
    if 'analysis_done' not in st.session_state:
        st.session_state['analysis_done'] = False
    if 'bill_text' not in st.session_state:
        st.session_state['bill_text'] = None
    
    main()
