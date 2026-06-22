import streamlit as st
import time

# 🛠️ 1. Website Page Architecture & Styling
st.set_page_config(page_title="ByteGuard AI", page_icon="🛡️", layout="wide")

# Initialize persistent mock statistics for the live view demo
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

# --- 💼 IF DISCOVERY IS TRUE, SHOW THE SECRET ADMIN PANEL ---
if is_admin:
    st.title("🛡️ BYTEGUARD ADMIN PANEL (🔒 SECURE MODE)")
    st.write("Full visibility and control over ByteGuard data streams.")
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
    st.subheader("🛠️ Backend Server Logs")
    st.info(f"System status: Operational. Connected to VirusTotal API Grid. Credits remaining: Healthy.")

# --- 🌐 IF LOGGED OUT, SHOW THE BEAUTIFUL CLIENT WEBPAGE ---
else:
    # COOL ASCII STREET ART LOGO
    st.code("""
 ██████╗ ██╗   ██╗████████╗███████╗ ██████╗ ██╗   ██╗ █████╗ ██████╗ ██████╗ 
 ██╔══██╗╚██╗ ██╔╝╚══██╔══╝██╔════╝██╔════╝ ██║   ██║██╔══██╗██╔══██╗██╔══██╗
 ██████╔╝ ╚████╔╝    ██║   █████╗  ██║  ███╗██║   ██║███████║██████╔╝██║  ██║
 ██╔══██╗  ╚██╔╝     ██║   ██╔══╝  ██║   ██║██║   ██║██╔══██║██╔══██╗██║  ██║
 ██████╔╝   ██║      ██║   ███████╗╚██████╔╝╚██████╔╝██║  ██║██║  ██║██████╔╝
 ╚══════╝   ╚═╝      ╚═╝   ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ 
                      [=== SECURITY SENTINEL ONLINE ===]
    """)
    
    # 🎨 GREEN GRAFFITI SMILEY FACES
    st.code("""
      .  .               .  .

     |  |             |  |
    |  |             |  |
   \____/           \____/
  /      \         /      \\

 |  O  O  |       |  O  O  |
 |    ^   |       |    ^   |
  \  --- /         \  --- /
   \____/           \____/
    """)
    
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

    # 🚀 FOUR TAB SYSTEM
    tab1, tab2, tab3, tab4 = st.tabs([
        "📧 EMAIL SCANNER (FREE)", 
        "📁 FILE SCANNER (PREMIUM)", 
        "⚡ SENTINEL ENGINE (PREMIUM)",
        "📊 BYTEGUARD VS NORTON"
    ])

    with tab1:
        st.header("Free Email Check Interface")
        st.write("Copy and paste suspicious email bodies below to check for hacker loops.")
        
        sender_input = st.text_input("Sender Domain/Email Address:", placeholder="support-update@netflix-verify-net.com")
        email_body_input = st.text_area("Body Text:", placeholder="Paste text messages here...")
        
        if st.button("Execute Free Inbox Scan"):
            if "netflix-verify" in sender_input.lower() or "urgent" in email_body_input.lower():
                st.error("❌ HACKER TRAP CAUGHT: This message mimics streaming alerts to lock your credentials!")
                st.session_state.stats["email_scans"] += 1
                st.session_state.stats["dangers_found"] += 1
            else:
                st.success("✅ SCAN COMPLETED: Email domain passes basic validation checks.")
                st.session_state.stats["email_scans"] += 1
                st.session_state.stats["safe_files"] += 1

        # History Display Log
        st.subheader("🗓️ SCAN HISTORY EVENTS")
        st.warning("⚠️ Warning Event Logged:\n\nSender: 'support-update@netflix-verify-net.com'\nMessage: 'Hey Please buy our new 70$ plan for a week thank you, Netflix Team...'")

    with tab2:
        st.header("Multi-Engine Archive Check")
        st.error("🔒 FEATURE LOCKED: File scanner requires premium level credentials.")
        st.write("Please click 'Activate Premium Tier' in the sidebar to connect to the global 70-engine scanner grid.")
        st.file_uploader("Upload binary or directory files...", disabled=True)

    with tab3:
        st.header("⚡ Sentinel Background Loop Engine")
        st.error("🔒 FEATURE LOCKED: Sentinel 24/7 background monitoring requires premium tier tracking.")
        st.write("Upgrade your plan to activate automated file log scans that run invisibly while your device sleeps or during your lunch break.")

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
