# Dictionary with my personal data

# Spanish
data_esp = {
	'name': 'Jorge',
	'surname': 'Ruiz',
	'surname2': 'López',
	'description': [
		'Me apasiona la informática y el análisis de datos orientado al desarrollo de herramientas que puedan transformar nuestra visión del mundo. Estoy especializándome en ámbitos como la inteligencia artificial, el procesamiento y análisis de grandes cantidades de datos, y el desarrollo de scripts de Python para automatizar tareas. También soy alumno interno en el departamento de Ingeniería y Tecnología de Computadores en mi universidad.',
		'Además, trabajo con aplicaciones que siguen un esquema de comunicación cliente/servidor en Python, por lo que tengo experiencia en el ámbito de las redes. A nivel personal, estoy interesado en el mundo de la ciberseguridad y estoy en proceso de formarme por mi cuenta.'
	],

	'education': [
		{'skill': 'Programación en diversos lenguajes',
   		 'description': 'Mis lenguajes principales son Python y R, pero me he formado autónomamente en C y C++. Me centro en la limpieza, tratamiento y análisis de datos, automatización de tareas, y desarrollo de aplicaciones.',
		 'skill_detail': ['Python', 'R', 'C', 'C++', 'HTML']},

		{'skill': 'Amplio conocimiento en Bases de Datos',
   		 'description': 'He trabajado con diversos tipos de Bases de Datos, tanto SQL como las principales bases NoSQL del momento. Las he integrado en proyectos y aplicaciones con Python.',
		 'skill_detail': ['SQL (Oracle)', 'Neo4j', 'MongoDB', 'Redis', 'HBase', 'Cassandra']},

		 {'skill': 'Limpieza y Análisis de Datos',
   		 'description': 'Soy capaz de extraer y formatear datos manejando distintos tipos de ficheros, además de aplicar técnicas de análisis para obtener métricas, gráficas o conclusiones que permitan tomar decisiones',
		 'skill_detail': ['Pandas', 'Matplotlib', 'Seaborn', 'R', 'JSON', 'CSV', 'Excel']},

		 {'skill': 'Análisis Matemático y Estadístico',
   		 'description': 'Mi formación incluye experiencia en el ámbito matemático, por lo que he desarrollado el pensamiento analítico y la disciplina que requiere este campo; además de tener una sólida base en estadística.',
		 'skill_detail': ['Numpy', 'Simpy', 'Álgebra', 'Optimización', 'Cálculo', 'LaTeX', 'Markdown', 'Estadística']},

		 {'skill': 'Machine Learning e Inteligencia Artificial',
   		 'description': 'Tengo experiencia en el desarrollo y aplicación de modelos a partir de datos previamente tratados, permitiendo realizar predicciones y ayudando a la toma de decisiones.',
		 'skill_detail': ['Scikit-Learn', 'Keras', 'Tensorflow', 'Python + R']},

		 {'skill': 'Herramientas colaborativas y trabajo en equipo',
   		 'description': 'Trabajo constantemente con Git y Google Collab, además de contribuir en proyectos de mayor envergadura como alumno interno, o colaborar con otros de mis compañeros. Soy muy activo en GitHub.',
		 'skill_detail': ['Git', 'GitHub', 'Google Collab', 'Docker', 'Trabajo en equipo']},

		 {'skill': 'Manejo de Sistemas Operativos basados en Linux',
   		 'description': 'Trabajo cómodamente en entornos de Linux. Estoy acostumbrado a interactuar con la terminal y con el shell, lo que supone un aumento en mi eficiencia al realizar ciertas tareas.',
		 'skill_detail': ['Bash', 'RegEx', 'Shell Scripting', 'SSH y administración remota', 'Gestión de permisos']},

		 {'skill': 'Iniciación en ciberseguridad',
   		 'description': 'Aunque mi formación no lo incluye, es un campo que me interesa y en el que me estoy formando por mi cuenta. Formo parte del club de ciberseguridad y hacking ético de mi universidad.',
		 'skill_detail': ['Local File Inclusion', 'Cracking', 'File Upload Attacks', 'SQL Injection', 'Redes']}
	],

	'experience': [
		{'type': 'Alumno Interno en el Departamento de Ingeniería y Tecnología de Computadores',
		 'date': '2024 - Actualidad',
		 'place': 'Universidad de Murcia, España',
		 'description': ['Tutelado por el Dr. José Rubén Titos.', 'Iniciación en el ámbito de la investigación científicos - Lectura y producción de "papers".', 'Participación en el desarrollo de herramientas para mejorar los recursos de una asignatura de mi propio grado.', 'Programación de utilidades para favorecer el aprendizaje automatizado.', 'Proyectos de análisis de grandes cantidades de datos de alumnos para mejorar la calidad de la asignatura.', 'Se pueden ver las actividades realizadas con detalle durante el curso 2024-25 en el informe.'],
		 'certificados': [
			{'nombre': 'Nombramiento Curso 24/25', 'file': 'nombramiento_alu_interno.pdf'},
			{'nombre': 'Informe Curso 24/25', 'file': 'informe_alu_interno_24-25.pdf'}
		 ]}
	],

	'studies': [
		{'type': 'Grado en Ciencia e Ingeniería de Datos',
		 'date': '2023 - Actualidad',
		 'place': 'Universidad de Murcia, España',
		 'description': ['Herramientas de análisis de datos avanzado, estadística, Machine Learning, tratamiento de datos, etc.', 'Aprendizaje con proyectos para poner en práctica los contenidos teóricos.', 'Realización de prácticas tanto individuales como en grupos.', 'En proceso - Nota media de 9.8 y 19 asignaturas con Matrícula de Honor.']},
		
		{'type': 'Bachillerato en Ciencias',
		 'date': '2021 - 2023',
		 'place': 'IES Ramón Arcas Meca, Lorca (Murcia)',
		 'description': ['Nota media de 10.', 'Graduado con Mención Honorífica en toda la etapa.', 'Premiado en la Olimpiada de Física (Universidad de Murcia) - 8º puesto.', 'Participación en talleres de debate y de música.'],
		 'certificados': ['informe_alu_interno.pdf']},
	],

	'languages': [
		{'lang': "Español", "level": "Lengua Materna", "certificate": ""},
		{'lang': "Inglés", "level": "Avanzado C1", "certificate": "AÑADIR"},  #"english_c1.pdf" dentro de static/files
		{'lang': "Francés", "level": "Intermedio Alto B2", "certificate": "AÑADIR"},
		{'lang': "Japonés", "level": "Básico", "certificate": ""}
	],

	'logos': [
		{"title": "Python", "file": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original-wordmark.svg"},
		{"title": "R", "file": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/rstudio/rstudio-original.svg"},
		{"title": "Oracle", "file": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/oracle/oracle-original.svg"},
    	{"title": "Docker", "file": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/docker/docker-plain-wordmark.svg"},
		{"title": "NumPy", "file": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/numpy/numpy-original-wordmark.svg"},
		{"title": "Matplotlib", "file": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/matplotlib/matplotlib-plain-wordmark.svg"},
		{"title": "Keras", "file": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/keras/keras-original-wordmark.svg"},
		{"title": "Scikit-learn", "file": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/scikitlearn/scikitlearn-original.svg"},
		{"title": "Git", "file": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/git/git-original-wordmark.svg"},
		{"title": "GitHub", "file": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/github/github-original-wordmark.svg"},
		{"title": "Google Cloud", "file": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/googlecloud/googlecloud-original-wordmark.svg"},
		{"title": "Bash", "file": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/bash/bash-original.svg"},
		{"title": "Linux", "file": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/linux/linux-original.svg"},
		{"title": "MongoDB", "file": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/mongodb/mongodb-original-wordmark.svg"},
		{"title": "Redis", "file": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/redis/redis-original-wordmark.svg"},
		{"title": "Cassandra", "file": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/cassandra/cassandra-original-wordmark.svg"},
		{"title": "Neo4j", "file": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/neo4j/neo4j-original-wordmark.svg"},
		{"title": "Anaconda", "file": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/anaconda/anaconda-original-wordmark.svg"},
		{"title": "Colab", "file": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/googlecolab/googlecolab-original.svg"}
	],

	'projects': [
		{'name': 'Bash Logger y Quiz', 
   		 'date': 'Colaborador; Junio 2025 - En marcha',
		 'description': 'Próximamente ',
		 'link': '',
		 'img': ''},

		 {'name': '', 
   		 'date': '',
		 'description': '',
		 'link': '',
		 'img': ''},

		 {'name': '', 
   		 'date': '',
		 'description': '',
		 'link': '',
		 'img': ''},
	],

	'contact': [
		{'name': 'LinkedIn', 
   		 'logo': 'https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/linkedin/linkedin-original.svg', 
		 'url': 'https://www.linkedin.com/in/jorge-ruiz-l%C3%B3pez-6a0101321/'},
		{'name': 'GitHub',
   		 'logo': 'https://img.icons8.com/?size=100&id=LoL4bFzqmAa0&format=png&color=000000',
		 'url': 'https://github.com/jorge-ruizl-um-es'},
		{'name': 'Gmail',
   		 'logo': 'https://img.icons8.com/?size=100&id=P7UIlhbpWzZm&format=png&color=000000',
		 'url': 'jorge.rulo2005@gmail.com'},
		{'name': 'Instagram',
   		 'logo': 'https://img.icons8.com/?size=100&id=32323&format=png&color=000000',
		 'url': 'https://www.instagram.com/jorgeruiz_5?igsh=endnY2ZseWk0YmUz'},
		{'name': 'Telegram',
   		 'logo': 'https://img.icons8.com/?size=100&id=63306&format=png&color=000000',
		 'url': 'https://t.me/jorgeruiz_5'}
	]
}

# English
data_eng = {
	'name': 'Jorge',
	'surname': 'Ruiz',
	'surname2': 'López',

	'contact': [
		{'name': 'LinkedIn', 
   		 'logo': 'https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/linkedin/linkedin-original.svg', 
		 'url': 'https://www.linkedin.com/in/jorge-ruiz-l%C3%B3pez-6a0101321/'},
		{'name': 'GitHub',
   		 'logo': 'https://img.icons8.com/?size=100&id=LoL4bFzqmAa0&format=png&color=000000',
		 'url': 'https://github.com/jorge-ruizl-um-es'},
		{'name': 'Gmail',
   		 'logo': 'https://img.icons8.com/?size=100&id=P7UIlhbpWzZm&format=png&color=000000',
		 'url': 'jorge.rulo2005@gmail.com'},
		{'name': 'Instagram',
   		 'logo': 'https://img.icons8.com/?size=100&id=32323&format=png&color=000000',
		 'url': 'https://www.instagram.com/jorgeruiz_5?igsh=endnY2ZseWk0YmUz'},
		{'name': 'Telegram',
   		 'logo': 'https://img.icons8.com/?size=100&id=63306&format=png&color=000000',
		 'url': 'https://t.me/jorgeruiz_5'}
	],

	'logos': [
		{"title": "Python", "file": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original-wordmark.svg"},
		{"title": "R", "file": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/rstudio/rstudio-original.svg"},
		{"title": "Oracle", "file": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/oracle/oracle-original.svg"},
    	{"title": "Docker", "file": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/docker/docker-plain-wordmark.svg"},
		{"title": "NumPy", "file": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/numpy/numpy-original-wordmark.svg"},
		{"title": "Matplotlib", "file": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/matplotlib/matplotlib-plain-wordmark.svg"},
		{"title": "Keras", "file": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/keras/keras-original-wordmark.svg"},
		{"title": "Scikit-learn", "file": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/scikitlearn/scikitlearn-original.svg"},
		{"title": "Git", "file": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/git/git-original-wordmark.svg"},
		{"title": "GitHub", "file": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/github/github-original-wordmark.svg"},
		{"title": "Google Cloud", "file": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/googlecloud/googlecloud-original-wordmark.svg"},
		{"title": "Bash", "file": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/bash/bash-original.svg"},
		{"title": "Linux", "file": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/linux/linux-original.svg"},
		{"title": "MongoDB", "file": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/mongodb/mongodb-original-wordmark.svg"},
		{"title": "Redis", "file": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/redis/redis-original-wordmark.svg"},
		{"title": "Cassandra", "file": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/cassandra/cassandra-original-wordmark.svg"},
		{"title": "Neo4j", "file": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/neo4j/neo4j-original-wordmark.svg"},
		{"title": "Anaconda", "file": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/anaconda/anaconda-original-wordmark.svg"},
		{"title": "Colab", "file": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/googlecolab/googlecolab-original.svg"}
	]

}