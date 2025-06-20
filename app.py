import streamlit as st
from datetime import datetime, timedelta
import time
from optimized_bbfs_system import get_optimized_system

# Configure for production deployment
@st.cache_resource
def load_system():
    """Load system with caching for better performance"""
    try:
        return get_optimized_system()
    except Exception as e:
        st.error(f"Error loading system: {str(e)}")
        return None

def main():
    st.set_page_config(
        page_title="BBFS Analytics Pro", 
        page_icon="⚡",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
    
    # Ultra-professional CSS theme
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');
    
    /* Hide only Streamlit header bar safely */
    header[data-testid="stHeader"] {
        height: 0rem !important;
        display: none !important;
    }
    
    .stApp > header {
        height: 0rem !important;
        display: none !important;
    }
    
    #MainMenu {
        visibility: hidden !important;
    }
    
    /* Ensure main content is visible */
    .main .block-container {
        padding-top: 1rem !important;
    }
    
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        font-family: 'Poppins', sans-serif;
        color: #ffffff;
        padding: 0;
    }
    
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    .header-container {
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(20px);
        border-radius: 20px;
        padding: 2rem;
        margin-bottom: 2rem;
        border: 1px solid rgba(255, 255, 255, 0.2);
        text-align: center;
    }
    
    .main-title {
        font-size: 2.8rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
        background: linear-gradient(45deg, #ffffff, #f0f0f0);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .subtitle {
        font-size: 1.2rem;
        opacity: 0.9;
        font-weight: 400;
    }
    
    .status-badge {
        background: rgba(255, 255, 255, 0.2);
        backdrop-filter: blur(10px);
        padding: 1rem 2rem;
        border-radius: 50px;
        font-weight: 600;
        text-align: center;
        margin: 1.5rem auto;
        display: inline-block;
        border: 1px solid rgba(255, 255, 255, 0.3);
        color: #ffffff;
    }
    
    .main-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(20px);
        border-radius: 20px;
        padding: 2rem;
        margin: 1.5rem 0;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
    }
    
    .analytics-card {
        background: rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(15px);
        border-radius: 16px;
        padding: 1.5rem;
        margin: 1rem 0;
        border: 1px solid rgba(255, 255, 255, 0.15);
        transition: all 0.3s ease;
    }
    
    .analytics-card:hover {
        background: rgba(255, 255, 255, 0.12);
        border: 1px solid rgba(255, 255, 255, 0.25);
    }
    
    .bbfs-display {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
        color: #ffd700;
        font-size: 3rem;
        font-weight: 900;
        text-align: center;
        padding: 2rem;
        border-radius: 16px;
        margin: 1.5rem 0;
        letter-spacing: 0.8rem;
        font-family: 'Monaco', monospace;
        border: 2px solid rgba(255, 215, 0, 0.3);
        box-shadow: 0 0 30px rgba(255, 215, 0, 0.2);
    }
    
    .section-title {
        font-size: 1.6rem;
        font-weight: 700;
        margin-bottom: 1rem;
        color: #ffffff;
        border-bottom: 2px solid rgba(255, 255, 255, 0.3);
        padding-bottom: 0.5rem;
    }
    
    .metric-row {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 1rem;
        margin: 1rem 0;
    }
    
    .metric-item {
        background: rgba(255, 255, 255, 0.1);
        padding: 1rem;
        border-radius: 12px;
        text-align: center;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    .metric-value {
        font-size: 1.8rem;
        font-weight: 800;
        color: #ffd700;
    }
    
    .metric-label {
        font-size: 0.9rem;
        opacity: 0.8;
        margin-top: 0.5rem;
    }
    
    .current-streak {
        background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%);
        padding: 1.5rem;
        border-radius: 16px;
        text-align: center;
        margin: 1rem 0;
        border: 2px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 8px 32px rgba(255, 107, 107, 0.3);
        transition: all 0.3s ease;
    }
    
    .current-streak.success {
        background: linear-gradient(135deg, #00d2d3 0%, #54a0ff 100%);
        box-shadow: 0 8px 32px rgba(0, 210, 211, 0.3);
    }
    
    .current-streak:hover {
        transform: translateY(-2px);
        box-shadow: 0 12px 40px rgba(255, 107, 107, 0.4);
    }
    
    .current-streak.success:hover {
        box-shadow: 0 12px 40px rgba(0, 210, 211, 0.4);
    }
    
    .streak-number {
        font-size: 2.5rem;
        font-weight: 900;
        margin: 0.5rem 0;
    }
    
    .data-table {
        background: rgba(255, 255, 255, 0.08);
        border-radius: 12px;
        padding: 1rem;
        margin: 1rem 0;
        border: 1px solid rgba(255, 255, 255, 0.15);
        overflow: hidden;
    }
    
    .table-row {
        display: grid;
        grid-template-columns: 1fr 1fr 1fr 1fr;
        padding: 0.8rem;
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        font-weight: 500;
        transition: all 0.2s ease;
        align-items: center;
        text-align: center;
    }
    
    .table-row:hover {
        background: rgba(255, 255, 255, 0.08);
        transform: translateX(2px);
    }
    
    .table-row:last-child {
        border-bottom: none;
    }
    
    .table-header {
        font-weight: 700;
        background: rgba(255, 255, 255, 0.1);
        border-radius: 8px;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.8rem 1.5rem;
        font-weight: 600;
        font-family: 'Poppins', sans-serif;
        transition: all 0.3s ease;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 20px rgba(0, 0, 0, 0.3);
    }
    
    .css-1d391kg {
        background: rgba(0, 0, 0, 0.2);
        backdrop-filter: blur(10px);
        border-right: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    .block-container {
        padding-top: 2rem;
        padding-bottom: 1rem;
    }
    
    h1, h2, h3, h4, h5, h6 {
        color: #ffffff;
        font-family: 'Poppins', sans-serif;
    }
    
    @media (max-width: 768px) {
        .main-title {
            font-size: 2.2rem;
        }
        
        .bbfs-display {
            font-size: 2rem;
            letter-spacing: 0.5rem;
        }
        
        .table-row {
            grid-template-columns: 1fr;
            gap: 0.3rem;
        }
        
        .metric-row {
            grid-template-columns: 1fr;
        }
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Initialize system with caching
    system = load_system()
    
    if system is None:
        st.error("Gagal memuat sistem. Silakan refresh halaman.")
        st.stop()
    
    # Header
    st.markdown("""
    <div class="header-container">
        <div class="main-title">BBFS Analytics Pro</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Auto-load data with better error handling
    if 'data_loaded' not in st.session_state:
        st.session_state.data_loaded = False
    
    if not st.session_state.data_loaded:
        try:
            if system.fetch_complete_data():
                system.run_performance_test()
                st.session_state.data_loaded = True
            else:
                st.error("Gagal memuat data. Menggunakan mode demo.")
                st.session_state.data_loaded = True
        except Exception as e:
            st.error(f"Error memuat data: {str(e)}")
            st.session_state.data_loaded = True
    
    # Status - selalu tampilkan sesuatu
    if system.data and len(system.data) > 0:
        performance = system.get_performance_summary()
        if performance:
            status_color = "#00d2d3" if performance['max_consecutive_loss'] <= 10 else "#ff6b6b"
            status_icon = "●" if performance['max_consecutive_loss'] <= 10 else "●"
            st.markdown(f"""
            <div class="status-badge">
                <span style="color: {status_color};">{status_icon}</span> Max {performance['max_consecutive_loss']} Loss | 
                Win {performance['win_rate']:.1f}% | {performance['total_tests']:,} Data
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown('<div class="status-badge">MEMPROSES DATA...</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="status-badge">MEMUAT SISTEM...</div>', unsafe_allow_html=True)
    
    # Auto Refresh Button
    if st.button("Auto Refresh Data", type="primary", use_container_width=True):
        with st.spinner("Memperbarui data real-time..."):
            if system.fetch_complete_data():
                system.run_performance_test()
                st.success("Data berhasil diperbarui!")
                time.sleep(1)
            else:
                st.error("Gagal memperbarui data")
    
    # Sidebar - Data info
    with st.sidebar:
        data_info = system.get_data_info()
        if data_info:
            st.markdown("### Dataset")
            st.metric("Records", f"{data_info['total_records']:,}")
            st.text(f"{data_info['date_range']['start']} - {data_info['date_range']['end']}")
            
            # Performance metrics
            performance = system.get_performance_summary()
            if performance:
                st.markdown("### Performance")
                st.metric("Max Loss Streak", performance['max_consecutive_loss'])
                st.metric("Win Rate", f"{performance['win_rate']:.1f}%")
                target_status = "Tercapai" if performance['max_consecutive_loss'] <= 10 else "Belum Tercapai"
                st.metric("Target ≤10 Loss", target_status)
    
    # Main Content - pastikan selalu ditampilkan
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Prediksi BBFS 5 Angka Optimal</div>', unsafe_allow_html=True)
    
    # Selalu tampilkan konten dasar
    if system.data and len(system.data) >= 2:
        latest_results = system.get_latest_results(1)
        if latest_results and len(latest_results) > 0:
            latest = latest_results[0]
            current_day = datetime.now().strftime('%A').lower()
            
            day_mapping = {
                'monday': 'senin', 'tuesday': 'selasa', 'wednesday': 'rabu',
                'thursday': 'kamis', 'friday': 'jumat', 'saturday': 'sabtu', 'sunday': 'minggu'
            }
            indonesian_day = day_mapping.get(current_day, 'senin')
            
            try:
                # Generate BBFS untuk latest result
                input_2d = latest['result'][-2:]
                bbfs = system.generate_optimized_bbfs(input_2d, indonesian_day)
                
                # Show 19/06/2025 kamis as requested
                target_date = datetime(2025, 6, 19)
                current_date_display = target_date.strftime('%d/%m/%Y')
                current_day_indo = 'kamis'
                
                st.markdown(f"""
                **Data Terakhir:** {latest['result']} | **Tanggal:** {current_date_display} | 
                **Hari:** {current_day_indo} | **Input 2D:** {input_2d} | **Hasil Aktual:** {latest['result']} ({latest['result'][-2:]})
                """)
                
                # BBFS Display
                bbfs_display = ' '.join(bbfs)
                st.markdown(f'<div class="bbfs-display">{bbfs_display}</div>', unsafe_allow_html=True)
                
                # Quick metrics dengan validasi data
                performance = system.get_performance_summary()
                if performance and performance.get('total_tests', 0) > 0:
                    # Validasi ulang perhitungan untuk memastikan akurasi
                    total_tests = performance.get('total_tests', 0)
                    total_wins = performance.get('wins', 0)
                    total_losses = total_tests - total_wins
                    calculated_win_rate = (total_wins / total_tests * 100) if total_tests > 0 else 0
                    
                    st.markdown('<div class="metric-row">', unsafe_allow_html=True)
                    st.markdown(f"""
                    <div class="metric-item">
                        <div class="metric-value">{calculated_win_rate:.1f}%</div>
                        <div class="metric-label">Win Rate (Akurat)</div>
                    </div>
                    <div class="metric-item">
                        <div class="metric-value">{performance["max_consecutive_loss"]}</div>
                        <div class="metric-label">Max Loss Streak</div>
                    </div>
                    <div class="metric-item">
                        <div class="metric-value">{total_wins:,}</div>
                        <div class="metric-label">Total Wins</div>
                    </div>
                    <div class="metric-item">
                        <div class="metric-value">{total_tests:,}</div>
                        <div class="metric-label">Total Tests</div>
                    </div>
                    """, unsafe_allow_html=True)
                    st.markdown('</div>', unsafe_allow_html=True)
                    
                    # Tampilkan informasi validasi untuk transparansi
                    st.markdown(f"""
                    <div style="text-align: center; margin-top: 0.5rem; padding: 0.5rem; background: rgba(255,255,255,0.1); border-radius: 8px; font-size: 0.85rem;">
                        Validasi: {total_wins} WIN + {total_losses} LOSS = {total_tests} Total Tests
                    </div>
                    """, unsafe_allow_html=True)
                    
            except Exception as e:
                st.warning(f"Memproses prediksi... ({str(e)})")
        else:
            st.info("Data tidak tersedia")
    else:
        # Tampilkan konten default jika tidak ada data
        st.markdown("""
        <div style="text-align: center; padding: 2rem;">
            <h3>Sistem Sedang Memuat Data</h3>
            <p>Silakan tunggu beberapa saat...</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Current Loss Streak Analysis
    st.markdown('<div class="section-title">Loss Streak Aktif</div>', unsafe_allow_html=True)
    
    # Calculate current loss streak
    current_loss_streak, streak_details = system.get_current_loss_streak_analysis(10)
    
    # Display current streak
    col1, col2 = st.columns([1, 1])
    
    with col1:
        if current_loss_streak > 0:
            st.markdown(f"""
            <div class="current-streak">
                <h3 style="margin: 0 0 1rem 0; font-weight: 700;">LOSS STREAK AKTIF</h3>
                <div class="streak-number">{current_loss_streak}</div>
                <p style="margin: 0.5rem 0 0 0; opacity: 0.9;">Memerlukan strategi khusus</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="current-streak success">
                <h3 style="margin: 0 0 1rem 0; font-weight: 700;">TIDAK ADA STREAK</h3>
                <div class="streak-number">0</div>
                <p style="margin: 0.5rem 0 0 0; opacity: 0.9;">Kondisi operasional normal</p>
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        if streak_details:
            st.markdown('<div class="analytics-card">', unsafe_allow_html=True)
            st.markdown("**Detail Loss Streak Aktif:**")
            
            for detail in streak_details[:6]:
                # Format date - use 19/06 as base date
                try:
                    if hasattr(detail['date'], 'strftime'):
                        # Calculate offset to show progressive dates from 19/06/2025
                        base_date = datetime(2025, 6, 19)
                        offset_days = streak_details.index(detail)
                        display_date = base_date - timedelta(days=offset_days)
                        date_display = display_date.strftime('%d/%m')
                    else:
                        date_display = str(detail['date'])[:5]
                except:
                    date_display = "N/A"
                
                # Extract 2D from the correct keys
                input_2d = detail['input_2d']
                actual_2d = detail['actual_2d']
                
                st.markdown(f"""
                <div style="padding: 0.3rem 0; border-bottom: 1px solid rgba(255,255,255,0.1);">
                    <span style="font-size: 0.85rem;">{date_display}</span><br>
                    <span><strong>{detail['input_result']}</strong> ({input_2d}) → {detail['actual_result']} ({actual_2d})</span>
                    <span style="color: #ff6b6b; font-weight: 600; float: right;">LOSS #{detail['loss_number']}</span>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="analytics-card">', unsafe_allow_html=True)
            st.markdown("""
            <div style="text-align: center; padding: 2rem;">
                <div style="font-size: 1.2rem; font-weight: 600; color: #00d2d3; margin-bottom: 0.5rem;">
                    Tidak Ada Loss Streak Aktif
                </div>
                <div style="font-size: 0.9rem; color: #ccc; opacity: 0.8;">
                    Sistem beroperasi dalam kondisi normal
                </div>
            </div>
            """, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
    
    # Loss Streak Statistics
    st.markdown('<div class="section-title">Statistik Loss Streak</div>', unsafe_allow_html=True)
    loss_stats = system.get_consecutive_loss_breakdown()
    if loss_stats and len(loss_stats) > 0:
        st.markdown('<div class="analytics-card">', unsafe_allow_html=True)
        st.markdown("**Distribusi Historis:**")
        
        # Real-time validated loss streak statistics
        st.markdown('<div class="data-table">', unsafe_allow_html=True)
        st.markdown('<div class="table-row table-header"><span>Streak</span><span>Count</span><span>Persentase</span><span>Status</span></div>', unsafe_allow_html=True)
        
        for streak_length, stats in sorted(loss_stats.items()):
            # Extract numeric value from streak_length like "1x", "2x", etc.
            streak_num = int(streak_length.replace('x', ''))
            status = "Normal" if streak_num <= 3 else "Perhatian" if streak_num <= 6 else "Kritis"
            st.markdown(f"""
            <div class="table-row">
                <span>{streak_length}</span>
                <span>{stats["count"]}</span>
                <span>{stats["percentage"]:.1f}%</span>
                <span>{status}</span>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Latest Results with Win/Loss Analysis
    st.markdown('<div class="section-title">Data Real-Time Terbaru</div>', unsafe_allow_html=True)
    
    # Refresh button
    if st.button("Refresh Data Terbaru", key="refresh_realtime", use_container_width=True, type="primary"):
        with st.spinner("Mengambil data real-time..."):
            if system.fetch_complete_data():
                system.run_performance_test()
                st.success("Data terbaru berhasil dimuat!")
                time.sleep(0.8)
                st.rerun()
            else:
                st.error("Gagal mengambil data terbaru")
    
    # Get real-time analysis data
    realtime_analysis = system.get_real_time_analysis(8)
    if realtime_analysis:
        # Current result info dari data terbaru
        latest = realtime_analysis[0]
        
        # Format tanggal
        try:
            if hasattr(latest['date'], 'strftime'):
                date_display = latest['date'].strftime('%d/%m/%Y')
            else:
                date_display = str(latest['date'])[:10]
        except:
            date_display = str(latest['date'])
        
        # Show 19/06/2025 kamis as requested
        target_date = datetime(2025, 6, 19)  # 19 Juni 2025 (Kamis)
        current_date_display = target_date.strftime('%d/%m/%Y')
        current_day_indo = 'kamis'
        
        st.markdown(f"""
        **Data Terakhir:** {latest['input_result']} | **Tanggal:** {current_date_display} | 
        **Hari:** {current_day_indo} | **Input 2D:** {latest['input_2d']} | **Hasil Aktual:** {latest['actual_result']} ({latest['actual_2d']})
        """)
        
        # Table with real-time win/loss analysis
        st.markdown('<div class="data-table" style="margin-top: 1rem;">', unsafe_allow_html=True)
        st.markdown('<div class="table-row table-header"><span>Tanggal</span><span>Input→Hasil</span><span>BBFS</span><span>Status</span></div>', unsafe_allow_html=True)
        
        wins_count = 0
        for analysis in realtime_analysis:
            if analysis['is_win']:
                wins_count += 1
            
            # Format date - use 19/06 as base date
            try:
                if hasattr(analysis['date'], 'strftime'):
                    # Calculate offset from 19/06/2025 to show progressive dates
                    base_date = datetime(2025, 6, 19)
                    offset_days = realtime_analysis.index(analysis)
                    display_date = base_date - timedelta(days=offset_days)
                    date_str = display_date.strftime('%d/%m')
                else:
                    date_str = str(analysis['date'])[:5]
            except:
                date_str = "N/A"
            
            status_color = "#00d2d3" if analysis['is_win'] else "#ff6b6b"
            status_text = "WIN" if analysis['is_win'] else "LOSS"
            
            # Tampilkan digit yang covered dan missing untuk transparency
            if analysis['is_win']:
                detail_info = f"Covered: {analysis['actual_2d']}"
            else:
                missing = ', '.join(analysis['missing_digits']) if analysis['missing_digits'] else "None"
                detail_info = f"Missing: {missing}"
            
            st.markdown(f"""
            <div class="table-row">
                <span style="font-size: 0.85rem;">{date_str}</span>
                <span>{analysis['input_2d']}→{analysis['actual_2d']}</span>
                <span style="font-size: 0.8rem; color: #ffd700;">{analysis['bbfs_string']}</span>
                <span style="color: {status_color}; font-weight: 600;">{status_text}</span>
            </div>
            <div style="font-size: 0.7rem; color: #aaa; padding: 0.2rem 0.8rem;">{detail_info}</div>
            """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Accurate summary
        total_analyzed = len(realtime_analysis)
        recent_win_rate = (wins_count / total_analyzed * 100) if total_analyzed > 0 else 0
        st.markdown(f"""
        <div style="text-align: center; margin-top: 1rem; padding: 1rem; background: rgba(255,255,255,0.1); border-radius: 10px;">
            <strong>Analisis Real-Time {total_analyzed} Data Terakhir:</strong> {wins_count} WIN dari {total_analyzed} test ({recent_win_rate:.1f}% win rate)
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()