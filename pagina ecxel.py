import os

# Write a complete, standalone, highly attractive HTML/CSS/JS file for the landing page
html_landing_code = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aprende Excel Cero a Avanzado — Domina la Prueba Técnica y Consigue Empleo</title>
    <!-- Google Fonts & Font Awesome Icons -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

    <style>
        :root {
            --primary: #059669;
            --primary-hover: #047857;
            --primary-light: #ecfdf5;
            --dark-blue: #0f172a;
            --slate-gray: #334155;
            --light-bg: #f8fafc;
            --card-border: #e2e8f0;
            --accent-orange: #f59e0b;
            --white: #ffffff;
            --shadow-sm: 0 2px 4px rgba(0,0,0,0.05);
            --shadow-md: 0 10px 25px -5px rgba(0,0,0,0.08), 0 8px 10px -6px rgba(0,0,0,0.01);
            --shadow-lg: 0 20px 30px -10px rgba(5, 150, 105, 0.15);
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Plus Jakarta Sans', sans-serif;
        }

        body {
            background-color: var(--light-bg);
            color: var(--slate-gray);
            line-height: 1.6;
        }

        /* Top Bar Urgency Banner */
        .top-banner {
            background: linear-gradient(90deg, #0f172a 0%, #065f46 100%);
            color: var(--white);
            text-align: center;
            padding: 10px 15px;
            font-size: 0.88rem;
            font-weight: 600;
        }

        .top-banner span {
            background: var(--accent-orange);
            color: #000;
            padding: 2px 8px;
            border-radius: 4px;
            font-size: 0.78rem;
            margin-right: 6px;
            font-weight: 700;
            text-transform: uppercase;
        }

        /* Header / Navbar */
        header {
            background-color: var(--white);
            border-bottom: 1px solid var(--card-border);
            padding: 16px 5%;
            display: flex;
            justify-content: space-between;
            align-items: center;
            position: sticky;
            top: 0;
            z-index: 1000;
        }

        .logo {
            display: flex;
            align-items: center;
            gap: 10px;
            font-weight: 800;
            font-size: 1.2rem;
            color: var(--dark-blue);
            text-decoration: none;
        }

        .logo i {
            color: var(--primary);
            font-size: 1.5rem;
        }

        .nav-btn {
            background-color: var(--primary);
            color: var(--white);
            padding: 10px 20px;
            border-radius: 8px;
            text-decoration: none;
            font-weight: 700;
            font-size: 0.9rem;
            transition: all 0.2s ease;
        }

        .nav-btn:hover {
            background-color: var(--primary-hover);
            transform: translateY(-1px);
        }

        /* Hero Section */
        .hero {
            padding: 60px 5% 80px 5%;
            max-width: 1200px;
            margin: 0 auto;
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 40px;
            align-items: center;
        }

        .hero-badge {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background-color: var(--primary-light);
            color: var(--primary);
            font-weight: 700;
            font-size: 0.85rem;
            padding: 6px 14px;
            border-radius: 20px;
            margin-bottom: 20px;
            border: 1px solid rgba(5, 150, 105, 0.2);
        }

        .hero-title {
            font-size: 2.5rem;
            font-weight: 800;
            color: var(--dark-blue);
            line-height: 1.2;
            margin-bottom: 18px;
        }

        .hero-title span {
            color: var(--primary);
            position: relative;
        }

        .hero-subtitle {
            font-size: 1.1rem;
            color: var(--slate-gray);
            margin-bottom: 30px;
        }

        /* Hero CTA Buttons Container */
        .hero-cta-group {
            display: flex;
            flex-direction: column;
            gap: 15px;
            margin-bottom: 30px;
        }

        .btn-main {
            background: linear-gradient(135deg, #059669 0%, #047857 100%);
            color: var(--white);
            padding: 16px 28px;
            border-radius: 10px;
            font-size: 1.05rem;
            font-weight: 800;
            text-decoration: none;
            text-align: center;
            box-shadow: var(--shadow-lg);
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
            border: none;
            cursor: pointer;
        }

        .btn-main:hover {
            transform: translateY(-2px);
            box-shadow: 0 22px 35px -10px rgba(5, 150, 105, 0.25);
        }

        .btn-secondary {
            background-color: var(--white);
            color: var(--dark-blue);
            border: 2px solid var(--card-border);
            padding: 14px 28px;
            border-radius: 10px;
            font-size: 0.98rem;
            font-weight: 700;
            text-decoration: none;
            text-align: center;
            transition: all 0.2s ease;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
        }

        .btn-secondary:hover {
            border-color: var(--primary);
            color: var(--primary);
            background-color: var(--primary-light);
        }

        /* Hero Visual Box */
        .hero-card {
            background: var(--white);
            border: 1px solid var(--card-border);
            border-radius: 16px;
            padding: 30px;
            box-shadow: var(--shadow-md);
            position: relative;
        }

        .card-header {
            display: flex;
            align-items: center;
            gap: 12px;
            margin-bottom: 20px;
        }

        .card-icon {
            width: 48px;
            height: 48px;
            background-color: var(--primary-light);
            color: var(--primary);
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.4rem;
        }

        .card-title-text {
            font-weight: 700;
            color: var(--dark-blue);
            font-size: 1.1rem;
        }

        .feature-list {
            list-style: none;
            display: flex;
            flex-direction: column;
            gap: 14px;
        }

        .feature-list li {
            display: flex;
            align-items: flex-start;
            gap: 12px;
            font-size: 0.95rem;
        }

        .feature-list i {
            color: var(--primary);
            font-size: 1.1rem;
            margin-top: 3px;
        }

        /* Key Metrics / Benefits Grid */
        .benefits-section {
            background-color: var(--white);
            padding: 70px 5%;
            border-top: 1px solid var(--card-border);
            border-bottom: 1px solid var(--card-border);
        }

        .section-title {
            text-align: center;
            font-size: 2rem;
            font-weight: 800;
            color: var(--dark-blue);
            margin-bottom: 12px;
        }

        .section-subtitle {
            text-align: center;
            color: var(--slate-gray);
            margin-bottom: 50px;
            font-size: 1rem;
        }

        .benefits-grid {
            max-width: 1100px;
            margin: 0 auto;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 30px;
        }

        .benefit-card {
            background-color: var(--light-bg);
            padding: 30px;
            border-radius: 12px;
            border: 1px solid var(--card-border);
            text-align: center;
            transition: transform 0.2s;
        }

        .benefit-card:hover {
            transform: translateY(-5px);
        }

        .benefit-icon {
            width: 60px;
            height: 60px;
            background-color: var(--white);
            color: var(--primary);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.5rem;
            margin: 0 auto 20px auto;
            box-shadow: var(--shadow-sm);
        }

        .benefit-title {
            font-size: 1.2rem;
            font-weight: 700;
            color: var(--dark-blue);
            margin-bottom: 10px;
        }

        /* Testimonials Section */
        .testimonials {
            padding: 80px 5%;
            max-width: 1100px;
            margin: 0 auto;
        }

        .testimonials-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 25px;
        }

        .testimonial-card {
            background-color: var(--white);
            padding: 25px;
            border-radius: 12px;
            border: 1px solid var(--card-border);
            box-shadow: var(--shadow-sm);
        }

        .stars {
            color: var(--accent-orange);
            margin-bottom: 12px;
            font-size: 0.9rem;
        }

        .review-text {
            font-style: italic;
            color: var(--slate-gray);
            font-size: 0.92rem;
            margin-bottom: 20px;
        }

        .user-info {
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .avatar {
            width: 42px;
            height: 42px;
            background-color: #cbd5e1;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 700;
            color: var(--dark-blue);
        }

        .user-details h4 {
            font-size: 0.95rem;
            color: var(--dark-blue);
        }

        .user-details p {
            font-size: 0.8rem;
            color: #64748b;
        }

        /* Modal Lead Magnet (Guía Gratis) */
        .modal-overlay {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(15, 23, 42, 0.7);
            display: none;
            justify-content: center;
            align-items: center;
            z-index: 2000;
            padding: 20px;
        }

        .modal-card {
            background-color: var(--white);
            border-radius: 16px;
            max-width: 480px;
            width: 100%;
            padding: 35px 30px;
            position: relative;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
            animation: modalFadeIn 0.3s ease;
        }

        @keyframes modalFadeIn {
            from { opacity: 0; transform: translateY(-20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .close-modal {
            position: absolute;
            top: 15px;
            right: 20px;
            background: none;
            border: none;
            font-size: 1.5rem;
            color: #64748b;
            cursor: pointer;
        }

        .modal-header {
            text-align: center;
            margin-bottom: 25px;
        }

        .modal-header i {
            font-size: 2.5rem;
            color: var(--primary);
            margin-bottom: 10px;
        }

        .modal-title {
            font-size: 1.4rem;
            font-weight: 800;
            color: var(--dark-blue);
            margin-bottom: 8px;
        }

        /* Footer */
        footer {
            background-color: var(--dark-blue);
            color: #94a3b8;
            text-align: center;
            padding: 30px 5%;
            font-size: 0.85rem;
            border-top: 1px solid #1e293b;
        }

        footer p {
            margin-bottom: 8px;
        }

        /* Responsive Breakpoints */
        @media (max-width: 850px) {
            .hero {
                grid-template-columns: 1fr;
                padding-top: 30px;
            }

            .hero-title {
                font-size: 2rem;
            }
        }
    </style>
</head>
<body>

    <!-- Top Urgency Banner -->
    <div class="top-banner">
        <span>OFERTA LIMITADA</span> Acceso con 50% de Descuento + Certificado de Finalización Incluido
    </div>

    <!-- Header Navigation -->
    <header>
        <a href="#" class="logo">
            <i class="fa-solid fa-file-excel"></i>
            <span>ProfesorDeExcel</span>
        </a>
        <a href="https://go.hotmart.com/F107115730Y?ap=8d3e" target="_blank" class="nav-btn">Inscribirme al Curso</a>
    </header>

    <!-- Hero Section -->
    <section class="hero">
        <div class="hero-left">
            <div class="hero-badge">
                <i class="fa-solid fa-briefcase"></i> Programa Especializado de Empleabilidad
            </div>
            <h1 class="hero-title">Domina Excel de Cero a Avanzado y <span>Consigue tu Próximo Empleo</span></h1>
            <p class="hero-subtitle">
                Supera las pruebas técnicas de selección, crea reportes gerenciales en minutos y añade un <strong>Certificado Oficial</strong> con validez internacional a tu CV y LinkedIn.
            </p>

            <div class="hero-cta-group">
                <!-- Botón Principal: Hotmart Affiliate Link Direct -->
                <a href="https://go.hotmart.com/F107115730Y?ap=8d3e" target="_blank" class="btn-main">
                    <i class="fa-solid fa-bolt"></i> INSCRIBIRME AL CURSO CON 50% DCTO.
                </a>

                <!-- Botón Secundario: Descarga PDF Gratis -->
                <a href="guia_excel_entrevistas.pdf" download="Guia_Excel_Pruebas_Tecnicas.pdf" class="btn-secondary" id="downloadPdfBtn">
                    <i class="fa-solid fa-file-pdf"></i> Descargar Guía Gratis (10 Preguntas de Entrevista)
                </a>
            </div>
        </div>

        <div class="hero-right">
            <div class="hero-card">
                <div class="card-header">
                    <div class="card-icon">
                        <i class="fa-solid fa-graduation-cap"></i>
                    </div>
                    <div>
                        <div class="card-title-text">Aprende Excel Cero a Avanzado</div>
                        <span style="font-size: 0.82rem; color: #64748b;">Acreditado por Hotmart</span>
                    </div>
                </div>

                <ul class="feature-list">
                    <li>
                        <i class="fa-solid fa-circle-check"></i>
                        <span><strong>Práctico y Laboral:</strong> Enfocado en resolver problemas reales de empresas.</span>
                    </li>
                    <li>
                        <i class="fa-solid fa-circle-check"></i>
                        <span><strong>Módulos Clave:</strong> BUSCARV/BUSCARX, Tablas Dinámicas, Dashboards y Macros.</span>
                    </li>
                    <li>
                        <i class="fa-solid fa-circle-check"></i>
                        <span><strong>Certificado de Finalización:</strong> Listo para subir a tu perfil de LinkedIn.</span>
                    </li>
                    <li>
                        <i class="fa-solid fa-circle-check"></i>
                        <span><strong>Acceso de Por Vida:</strong> Repasa el contenido antes de cada entrevista laboral.</span>
                    </li>
                </ul>
            </div>
        </div>
    </section>

    <!-- Benefits Section -->
    <section class="benefits-section">
        <h2 class="section-title">¿Por qué este curso asegura tu éxito laboral?</h2>
        <p class="section-subtitle">Diseñado específicamente para cubrir las exigencias de los reclutadores y departamentos de Selección.</p>

        <div class="benefits-grid">
            <div class="benefit-card">
                <div class="benefit-icon">
                    <i class="fa-solid fa-shield-halved"></i>
                </div>
                <h3 class="benefit-title">Confianza en Pruebas</h3>
                <p>Aprende exactamente qué fórmulas evaluar en cada caso para responder las pruebas con agilidad y precisión.</p>
            </div>

            <div class="benefit-card">
                <div class="benefit-icon">
                    <i class="fa-solid fa-certificate"></i>
                </div>
                <h3 class="benefit-title">Certificado Oficial</h3>
                <p>Destaca tu Currículum Vitae sobre cientos de postulantes demostrando tus conocimientos validados.</p>
            </div>

            <div class="benefit-card">
                <div class="benefit-icon">
                    <i class="fa-solid fa-clock"></i>
                </div>
                <h3 class="benefit-title">Ahorra Horas de Trabajo</h3>
                <p>Automatiza tareas repetitivas y limpia bases de datos caóticas en cuestión de segundos.</p>
            </div>
        </div>
    </section>

    <!-- Testimonials Section -->
    <section class="testimonials">
        <h2 class="section-title">Lo que dicen nuestros alumnos contratados</h2>
        <p class="section-subtitle">Profesionales que lograron superar sus pruebas de selección gracias al programa.</p>

        <div class="testimonials-grid">
            <div class="testimonial-card">
                <div class="stars">
                    <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
                </div>
                <p class="review-text">"Tenía una entrevista para un puesto de Analista Junior y me pidieron una prueba de Excel en vivo. Gracias a los módulos de Tablas Dinámicas y BUSCARV, la pasé sin problemas."</p>
                <div class="user-info">
                    <div class="avatar">AG</div>
                    <div class="user-details">
                        <h4>Ana Gómez</h4>
                        <p>Analista Junior — Contratada</p>
                    </div>
                </div>
            </div>

            <div class="testimonial-card">
                <div class="stars">
                    <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
                </div>
                <p class="review-text">"La guía gratuita me ayudó a entender lo básico, pero el curso completo con certificado fue lo que me dio el impulso final para subir mi perfil a LinkedIn y recibir ofertas."</p>
                <div class="user-info">
                    <div class="avatar">CM</div>
                    <div class="user-details">
                        <h4>Carlos Mendoza</h4>
                        <p>Asistente Administrativo</p>
                    </div>
                </div>
            </div>

            <div class="testimonial-card">
                <div class="stars">
                    <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
                </div>
                <p class="review-text">"Muy bien explicado y directo al grano. Las plantillas que entregan dentro del curso me ahorran horas de trabajo todos los días en la oficina."</p>
                <div class="user-info">
                    <div class="avatar">VR</div>
                    <div class="user-details">
                        <h4>Valeria Rivas</h4>
                        <p>Recién Graduada</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Modal Lead Magnet / Confirmación de Descarga -->
    <div class="modal-overlay" id="downloadModal">
        <div class="modal-card">
            <button class="close-modal" id="closeModalBtn">&times;</button>
            <div class="modal-header">
                <i class="fa-solid fa-circle-check"></i>
                <h3 class="modal-title">¡Tu Guía PDF se está descargando!</h3>
                <p style="font-size: 0.9rem; color: #64748b;">Revisa la carpeta de descargas en tu dispositivo.</p>
            </div>
            <div style="background-color: var(--primary-light); padding: 18px; border-radius: 10px; text-align: center; margin-bottom: 20px; border: 1px solid rgba(5,150,105,0.2);">
                <p style="font-size: 0.95rem; font-weight: 700; color: var(--dark-blue); margin-bottom: 8px;">
                    ¿Quieres acelerar tu aprendizaje y certificar tu nivel en Excel?
                </p>
                <p style="font-size: 0.85rem; color: var(--slate-gray);">
                    Aprovecha el 50% de descuento en la formación completa Cero a Avanzado por tiempo limitado.
                </p>
            </div>
            <a href="https://go.hotmart.com/F107115730Y?ap=8d3e" target="_blank" class="btn-main" style="width: 100%;">
                <i class="fa-solid fa-graduation-cap"></i> VER TEMARIO Y CERTIFICARME
            </a>
        </div>
    </div>

    <!-- Footer -->
    <footer>
        <p>&copy; 2026 ProfesorDeExcel. Todos los derechos reservados.</p>
        <p style="font-size: 0.78rem;">Este sitio no forma parte ni está respaldado por TikTok o Meta Inc. El acceso al producto se realiza de forma segura a través de la plataforma de Hotmart.</p>
    </footer>

    <!-- JavaScript Interactivo -->
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const downloadBtn = document.getElementById('downloadPdfBtn');
            const downloadModal = document.getElementById('downloadModal');
            const closeModalBtn = document.getElementById('closeModalBtn');

            // Abrir modal de recomendación cuando descargan la guía
            if (downloadBtn) {
                downloadBtn.addEventListener('click', function() {
                    setTimeout(function() {
                        downloadModal.style.display = 'flex';
                    }, 800);
                });
            }

            // Cerrar modal
            if (closeModalBtn) {
                closeModalBtn.addEventListener('click', function() {
                    downloadModal.style.display = 'none';
                });
            }

            // Cerrar modal haciendo clic fuera de la tarjeta
            window.addEventListener('click', function(e) {
                if (e.target === downloadModal) {
                    downloadModal.style.display = 'none';
                }
            });
        });
    </script>
</body>
</html>
"""

# Save to html file
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_landing_code)

print("Landing Page index.html created successfully!")