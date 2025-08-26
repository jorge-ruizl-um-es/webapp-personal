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
		 'skill_detail': ['Git', 'GitHub', 'Google Collab', 'Jupyter Notebook', 'Docker', 'Trabajo en equipo']},

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
		 'img': 'bash-logger.png',
		 'technologies': ['Python', 'Bash', 'Comunicación Cliente-Servidor', 'Git']},

		 {'name': 'Análisis Estadístico de la Pokédex Nacional', 
   		 'date': 'Autor; Enero 2025 - Junio 2025',
		 'description': 'El proyecto consiste en un análisis de las 1025 especies de Pokémon existentes, centrándonos en atributos categóricos (nombre, tipo, etc.) y, sobre todo, numéricos (HP, ataque, defensa, etc.). El objetivo fue encontrar patrones o relaciones ocultas entre los individuos, desentrañando de forma matemática y rigurosa la lógica detrás de estos videojuegos.\nSe aplican técnicas de Análisis Estadístico y Machine Learning para el estudio del dataset, a la vez que se ofrecen conclusiones orientadas al funcionamiento del juego. Además, el estudio converge en el desarrollo de una herramienta que permite ofrecer recomendaciones automatizadas e inteligentes de Pokémon con los que completar un equipo de 6.\nTodo está documentado en un PDF cuidadosamente formateado con todo el análisis y razonamientos o conclusiones pertinentes. Se incluyen los fragmentos de código más relevantes, pudiéndose ver completo en el fichero .qmd.',
		 'link': 'https://github.com/jorge-ruizl-um-es/pokedex-analysis.git',
		 'img': 'pokemon.jpg',
		 'technologies': ['R', 'LaTeX', 'Análisis Exploratorio de Datos', 'Análisis de Componentes Principales', 'Clustering Particional y Jerárquico', 'Regresión']},

		 {'name': 'Página web personal interactiva', 
   		 'date': 'Autor; Agosto 2025',
		 'description': 'Este proyecto es una aplicación web personal desarrollada con Flask que funciona como un currículum interactivo y bilingüe (español e inglés). A través de plantillas HTML con Bootstrap y datos almacenados en diccionarios, la web muestra información académica, experiencia, proyectos, habilidades, idiomas y enlaces de contacto.\nIncluye una página inicial para seleccionar el idioma, secciones organizadas y dinámicas (como carruseles para estudios o habilidades) y la posibilidad de descargar el CV en PDF, ofreciendo una carta de presentación moderna y navegable para mostrar mi trayectoria profesional y personal.\nSe trata de un primer proyecto sencillo para iniciarme en la programación de aplicaciones web, combinando aspectos básicos del diseño y desarrollo tanto en FrontEnd como en BackEnd.',
		 'link': 'https://github.com/jorge-ruizl-um-es/webapp-personal.git',
		 'img': 'web.png',
		 'technologies': ['Python', 'Flask', 'HTML', 'Bootstrap', 'CSS']},


		 {'name': 'Predicción de Visibilidad en los Lagos de Covadonga', 
   		 'date': 'Autor; Junio 2025 - Agosto 2025',
		 'description': 'Debido al problema que afrontan muchos turistas cada año al querer visitar una zona con un clima tan impredecible como pueden ser los Lagos de Covadonga (Asturias), se propone un estudio basado en datos y medidas reales para tratar de prever las condiciones de visibilidad a causa de la niebla. Se extraen datos históricos directamente de la API de la AEMET y de la observación directa de la zona para, a partir de la aplicación de diversos modelos de Machine Learning, ofrecer una predicción sobre la visibilidad en base a las previsiones introducidas para el día deseado.\nEl proyecto incluye la limpieza y tratamiento previo de los datos, la organización de los mismos, y el uso de diversas librería de Python relacionadas con Machine Learning para el entrenamiento, evaluación de resultados y comparación de distintos modelos conocidos.\n También se introduce el uso de un LLM ejecutado en local para el procesamiento previo de los datos',
		 'link': 'https://github.com/jorge-ruizl-um-es/fog-prediction.git',
		 'img': 'lagos.jpg',
		 'technologies': ['Python', 'Pandas', 'Matplotlib', 'Seaborn', 'Scikit-Learn', 'Keras', 'APIs', 'Ollama']},

		 {'name': 'Autocorrector de Comandos de Bash', 
   		 'date': 'Autor; Diciembre 2024 - Abril 2024',
		 'description': 'Esta herramienta forma parte de un proyecto de mayor envergadura en el que he colaborado. Consiste en un primer prototipo de un procesador y autocorrector de comandos de Bash. A partir de exámenes de la asignatura de Fundamentos de Computadores de la Facultad de Informática de la UMU, ofrecidos en formato de notebook de Jupyter, se extraen las soluciones correctas y las respuestas ofrecidas por cada alumno. Se va procesando pregunta por pregunta, detectando, en caso de que esté mal, el tipo de error cometido.\nSe ofrecen posteriormente distintos resúmenes en formato CSV que pueden ayudar a observar los resultados de un examen de manera directa, procesándolos en unos pocos segundos. Esta herramienta puede extenderse para usarse como un módulo autocorrector de comandos Bash que proporcione feedback automático (señalar los tipos de error cometidos sin decir al solución).',
		 'link': 'https://github.com/jorge-ruizl-um-es/bash-autocorrector.git',
		 'img': 'bash.png',
		 'technologies': ['Python', 'Bash', 'Jupyter Notebook', 'JSON', 'CSV', 'Git']}
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