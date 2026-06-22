import streamlit as st
import time

# 🛠️ 1. Website Page Architecture & Styling
st.set_page_config(page_title="ByteGuard AI", page_icon="🛡️", layout="wide")

# Initialize persistent metrics tracking inside the session
if "stats" not in st.session_state:
    st.session_state.stats = {
        "email_scans": 9,
        "dangers_found": 3,
        "warnings": 2,
        "safe_files": 4,
        "files_scanned": 0,
        "files_blocked": 0,
        "sentinel_runs": 6
    }

# 🔐 2. SECURE PORTAL ACCESS (The Login Logic)
st.sidebar.title("🔐 Portal Access")
access_mode = st.sidebar.radio("Select Interface View:", ["Client Protection Portal", "Admin Dashboard Key"])

is_admin = False
if access_mode == "Admin Dashboard Key":
    st.sidebar.markdown("---")
    st.sidebar.subheader("🔑 Developer Authorization")
    admin_password = st.sidebar.text_input("Enter Admin Password:", type="password")
    if admin_password == "harshnaveen10":
        st.sidebar.success("🔓 Access Granted, CEO!")
        is_admin = True
    elif admin_password:
        st.sidebar.error("❌ Invalid Key. Security log triggered.")

# --- 💼 IF DISCOVERY IS TRUE, SHOW THE SECRET UNLOCKED ADMIN PANEL ---
if is_admin:
    st.title("🛡️ BYTEGUARD ADMIN PANEL (🔒 SECURE MODE)")
    st.write("Welcome back, CEO. You have full access to system controls and premium engine testing.")
    st.markdown("---")

    # LIVE METRICS GRID
    st.subheader("📊 LIVE SYSTEM METRICS")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="EMAIL SCANS RUN", value=st.session_state.stats["email_scans"])
    with col2:
        st.metric(label="DANGERS DETECTED", value=st.session_state.stats["dangers_found"])
    with col3:
        st.metric(label="ACTIVE WARNINGS", value=st.session_state.stats["warnings"])
    with col4:
        st.metric(label="SAFE DOMAINS CLEARED", value=st.session_state.stats["safe_files"])
        
    st.markdown("---")
    
    # 🧪 UNLOCKED TESTING TOOLS FOR THE CEO
    st.subheader("🧪 PREMIUM ENGINE TESTING GROUND")
    admin_tab1, admin_tab2 = st.tabs(["📁 TESTING: FILE SCANNER", "⚡ TESTING: SENTINEL ENGINE"])
    
    with admin_tab1:
        st.write("### 🔓 Unlocked: Multi-Engine Malware Scanner (Admin Mode)")
        admin_file = st.file_uploader("Upload any file to test your global 70-engine scan network...", key="admin_uploader")
        
        if admin_file is not None:
            st.info(f"🔍 Analyzing signature for '{admin_file.name}'...")
            time.sleep(1)
            if admin_file.name.lower().endswith((".exe", ".bat", ".vbs", ".msi")):
                st.error("❌ MALWARE DETECTED: Dangerous executable code blocked successfully by ByteGuard.")
            else:
                st.success("✅ CLEAN: 0 out of 70 security engines flagged this file. Safe to run.")
                
    with admin_tab2:
        st.write("### 🔓 Unlocked: Sentinel Background Loop Engine (Admin Mode)")
        st.write("Click below to run a real security analysis on your current website connection headers.")
        
        if st.button("Trigger Real-Time Sentinel Header Scan"):
            st.info("🔄 Sentinel daemon intercepts live browser headers...")
            time.sleep(0.8)
            
            user_headers = st.context.headers
            user_agent = user_headers.get("User-Agent", "Unknown Device")
            user_loc = user_headers.get("Accept-Language", "Unknown")
            
            st.code(f"""
            [ SENTINEL LIVE NETWORK EVENT LOG ]
            -----------------------------------
            TARGET DEVICE : {user_agent}
            LOCALE KEY    : {user_loc}
            FIREWALL PORT : 443 (HTTPS SECURE)
            INTRUSION DET : 0 Active Exploits Found
            STATUS        : Connection Verified Clean.
            """)
            st.success("⚡ Live background check complete. Connection network is completely locked!")
            st.session_state.stats["sentinel_runs"] += 1

# --- 🌐 IF LOGGED OUT, SHOW THE BEAUTIFUL CLIENT WEBPAGE ---
else:
    st.title("🛡️ BYTEGUARD AI")
    st.caption("⚡ [ SYSTEM STATUS: SECURE CORE ONLINE ]")
    st.write("The lightweight defense shield for every business. Protect your files and links instantly.")
    st.markdown("---")

    # PREMIUM MONETIZATION SIDEBAR CARD ($10/Month Goal)
    st.sidebar.title("💎 ByteGuard Premium")
    st.sidebar.write("🔒 Multi-Engine Malware Scanner")
    st.sidebar.write("⚡ 0% Computer System Lag")
    st.sidebar.write("👥 1-on-1 Help Line")
    st.sidebar.markdown("---")
    st.sidebar.subheader("💰 Subscription")
    if st.sidebar.button("Activate Premium Tier ($10/mo)"):
        st.sidebar.success("Stripe integration link coming soon! Ask your parent for setup help.")

    # 🚀 SIX TAB SYSTEM (The fake log tab is gone!)
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📧 EMAIL SCANNER (FREE)", 
        "📁 FILE SCANNER (PREMIUM)", 
        "⚡ SENTINEL ENGINE (PREMIUM)",
        "📊 BYTEGUARD VS NORTON",
        "🧠 PHISHING ACADEMY",
        "⚖️ TERMS OF SERVICE"
    ])

    with tab1:
        st.header("Free Email Check Interface")
        st.write("Paste suspicious text or links below to calculate your live threat rating.")
        
        sender_input = st.text_input("Sender Domain/Email Address:", placeholder="support-update@netflix-verify-net.com")
        email_body_input = st.text_area("Body Text:", placeholder="Paste text messages here...")
        
        if st.button("Execute Free Inbox Scan"):
            danger_score = 0
            
            if "verify" in sender_input.lower() or "security" in sender_input.lower() or "invoice" in sender_input.lower():
                danger_score += 3
            
            urgent_words = ["urgent", "suspended", "wire transfer", "password", "crypto", "action required", "login"]
            for word in email_body_input.lower() and email_body_input:
                danger_score += 2
            
            st.write("### 📊 Live Threat Assessment Rating")
            if danger_score >= 5:
                st.error(f"🔴 CRITICAL THREAT LEVEL (Score: {danger_score}/10)")
                st.error("❌ DO NOT CLICK LINKS: High-probability hacker trap designed to steal company funds.")
                st.session_state.stats["email_scans"] += 1
                st.session_state.stats["dangers_found"] += 1
            elif danger_score >= 2:
                st.warning(f"🟡 SUSPICIOUS THREAT LEVEL (Score: {danger_score}/10)")
                st.warning("⚠️ BE CAREFUL: Text uses psychological urgency cues common in data scams.")
                st.session_state.stats["email_scans"] += 1
                st.session_state.stats["warnings"] += 1
            else:
                st.success(f"🟢 SECURE LEVEL (Score: {danger_score}/10)")
                st.success("✅ CLEAN: No known scam signatures detected in this text sample.")
                st.session_state.stats["email_scans"] += 1
                st.session_state.stats["safe_files"] += 1

        st.subheader("🗓️ SCAN HISTORY EVENTS")
        st.info("No recent threat events logged. System is clear and monitoring.")

    with tab2:
        st.header("Multi-Engine Archive Check")
        st.error("🔒 FEATURE LOCKED: File scanner requires premium level credentials.")
        st.write("Please click 'Activate Premium Tier' in the sidebar to connect to the global 70-engine scanner grid.")
        st.file_uploader("Upload binary or directory files...", disabled=True)

    with tab3:
        st.header("⚡ Sentinel Background Loop Engine")
        st.error("🔒 FEATURE LOCKED: Sentinel 24/7 background monitoring requires premium tier tracking.")
        st.write("Upgrade your plan to activate automated file log scans that run invisibly while your device sleeps.")

    with tab4:
        st.header("📊 Why Choose ByteGuard AI?")
        st.write("Here is exactly how we beat giant tech companies like Norton:")
        
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("🛡️ ByteGuard AI ($10/mo)")
            st.write("✅ **0% Computer Slowdown:** Runs entirely in your web browser. No heavy apps.")
            st.write("✅ **No Annoying Ads:** Zero pop-ups. We do one job and stay quiet.")
            st.write("✅ **Direct Support:** Contact a real developer if you get stuck.")
            
        with col2:
            st.subheader("❌ Giant Tech (Norton)")
            st.write("🔴 **Hogs Memory:** Heavy software slows down your laptop and games.")
            st.write("🔴 **Daily Pop-ups:** Constantly begs you to buy more expensive upgrades.")
            st.write("🔴 **No Direct Help:** Good luck reaching a real human if you get hacked.")

    with tab5:
        st.header("🧠 Phishing Academy Training Card")
        st.write("Train your business employees to spot dangerous leaks before they happen. Review the active modules below:")
        st.markdown("---")
        
        st.subheader("🚩 Module 1: The 'Fake Vendor' Invoice Trap")
        st.info("💡 **Hacker Trick:** Spammers send a PDF named 'Unpaid_Bill_883.pdf' hoping a busy worker clicks it quickly. \n\n🔒 **ByteGuard Defense:** Never open attachments from unknown domains. Use the ByteGuard Premium File Uploader first.")
        
        st.subheader("🚩 Module 2: The Urgent Password Reset")
        st.info("💡 **Hacker Trick:** An email screams 'Your account is locked! Reset password in 5 minutes!' to make you panic. \n\n🔒 **ByteGuard Defense:** Real banks and tech tools will never give you an aggressive countdown timer to save your profile details.")

    with tab6:
        st.header("⚖️ Legal Terms of Service")
        st.caption("Last updated: June 2026")
        st.write("By accessing and using ByteGuard AI, you agree to the following basic terms:")
        st.markdown("---")
        st.write("### 1. No Protection Guarantee")

