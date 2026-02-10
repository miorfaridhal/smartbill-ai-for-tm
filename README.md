# SmartBill AI - TM Bill Analyzer

A Streamlit web application that helps users understand their Telekom Malaysia (TM) bills through AI-powered analysis.

## Features

- 📄 **PDF Upload**: Upload your TM/Unifi bill in PDF format
- 🔍 **Intelligent Analysis**: Automatic extraction and analysis of bill information
- 💡 **Smart Insights**: Get clear explanations of charges and recommendations
- 📊 **Visual Dashboard**: Easy-to-read breakdown of your bill
- 💳 **Payment Options**: Quick access to payment methods
- 📥 **Download Report**: Export your analysis as a text report

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Setup Steps

1. **Clone or download this project**

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run smartbill_app.py
   ```

4. **Access the app**
   - The app will automatically open in your browser
   - Or navigate to `http://localhost:8501`

## Usage

1. **Upload Your Bill**
   - Click on the file upload area
   - Select your TM bill PDF file
   - Supported: Unifi Mobile, Unifi Home, Unifi Air, Streamyx bills

2. **Analyze**
   - Click the "Analyze Bill" button
   - Wait for the analysis to complete (usually a few seconds)

3. **Review Insights**
   - View your bill summary
   - Check the charges breakdown
   - Read recommendations and things to check
   - See payment options

4. **Download Report** (Optional)
   - Click "Download Analysis Report" to save the analysis as a text file

## Supported Bill Types

- ✅ Unifi Mobile postpaid bills
- ✅ Unifi Home broadband bills
- ✅ Unifi Air bills
- ✅ Streamyx bills
- ✅ All TM postpaid services

## Project Structure

```
.
├── smartbill_app.py       # Main Streamlit application
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## Key Functions

### `extract_text_from_pdf(pdf_file)`
Extracts text content from uploaded PDF files using PyPDF2.

### `parse_bill_info(bill_text)`
Parses key information from bill text:
- Account number
- Bill date
- Total amount
- Due date
- Previous balance
- Current charges

### `analyze_bill(bill_text)`
Generates comprehensive bill analysis including:
- Summary
- Charges breakdown
- Changes explanation
- Recommendations

## Technical Details

- **Framework**: Streamlit 1.31.0
- **PDF Processing**: PyPDF2 3.0.1
- **Python Version**: 3.8+

## Privacy & Security

- All processing is done locally
- No data is stored on external servers
- Bill information is only kept in session memory
- Session data is cleared when you close the browser

## Customization

You can customize the app by modifying:

1. **Color Scheme**: Edit the CSS in the `st.markdown()` section
2. **Analysis Logic**: Modify the `analyze_bill()` function
3. **Parsing Rules**: Update the `parse_bill_info()` function
4. **UI Layout**: Adjust the column layouts and sections

## Troubleshooting

### PDF Not Reading Correctly
- Ensure the PDF is not password-protected
- Check if the PDF is a scanned image (OCR may be needed)
- Verify the file is not corrupted

### Missing Dependencies
```bash
pip install --upgrade -r requirements.txt
```

### Port Already in Use
```bash
streamlit run smartbill_app.py --server.port 8502
```

## Future Enhancements

- [ ] OCR support for scanned PDFs
- [ ] Multi-language support (Malay/English)
- [ ] Bill comparison across months
- [ ] Export to PDF report
- [ ] Email notification for due dates
- [ ] Integration with payment gateways
- [ ] Usage pattern analysis
- [ ] Bill prediction for next month

## Disclaimer

This is an unofficial tool and is not affiliated with Telekom Malaysia Berhad. 
The analysis provided is for informational purposes only. Always verify the 
information with your official TM bill and contact TM customer service for 
any billing disputes.

## License

MIT License - Feel free to use and modify for your projects.

## Support

For issues or questions:
1. Check the troubleshooting section
2. Review the TM official documentation
3. Contact TM customer service for billing-specific queries

## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

---

Made with ❤️ for TM customers
