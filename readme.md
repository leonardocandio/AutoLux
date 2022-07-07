# AutoLux

# Creadores

* Max Antúnez
* Leonardo Candio
* Renato Cernades
* Ronaldo Flores

**==================================**
# BLUEPRINTS
**CADA RESPONSE CONTIENE :**
    -**code:***Es el Status de la petición*
    -**Success***Nos indica si nuestra peticon fue exitosa*
**========**
# FORUM_routes:
**URL:**"/posts"
-**paginate**:
    Se encarga de la paginación
    parámetros: page(URL), entero
-**get_forum**:
    Se encarga de retornar todo el forum
    methods= GET
-**create_post**:
    realiza los post de los forum
    parámetros: JSON(post_body string, post_title string)
    retorna: retorna los posts y el total
    methods= POST
-**delete_post**:
    Elimina el post
    parámetros: JSON(post_id integer, post_body string y post_title string)
    retorna: el post_id, eliminado y los restos 
    methods= DELETE
-**update_post**:
    Sube el post
    parámetros: JSON(post_id integer, post_body string y post_title string)
    retorna: el post_id y el total
    methods= PATCH
-**get_post**:
    obtiene el post por el id (URL)
    parámetros : id de post 
    methods= GET
-**create_comment**:
    crea el comentario
    parámetros: id de post (URL) ,JSON(comment_body string)
    retorna: el comentario, id y total de los comentarios
    methods= POST
-**delete_comment**:
    Elimina el comentario
    parámetros: id de post (URL), JSON(comment_id string)
    retorna: el comentario, id y total de los comentarios
    methods= DELETE
-**update_comment**:
    Sube el comentario
    parámetros: id de post (URL), JSON(comment_id integer, comment_body string)
    retorna: el comentario, id y total de los comentarios 
    methods= PATCH

**========**
# HOME_routes:
-**Home_page**:
    selecciona aleatoriamente un auto y un articulo en un rango de 6
    methods= POST
-**get_brands**:
    obtiene las marcas de los autos.
    retorna: un response que contiene a cada marca en un diccionario con el id
-**inject_permissions**:
    ...
-**before_request**:
    ...  

**========**
# NEW_routes
- **home**:
    render_templatede de 'news.html' y articles
- **article_page**:
    render_templatede de 'see_more_news.html' y articles
- **add_news**:
    retorna add news
- **delete_news**:
    retorna delete news
- **inject_permissions**:
    retorna diccionario de Permission
- **before_request**:
    si el user no esta identificado retorna abort(401)

**========**
# Shop_routes
**URL:**"/cars"
- **paginate**:
    ...
- **paginate_array**:
    ...
- **get_cars:**:
    recorre todos los Car 
    retorna: los cars, el total de cars, y los n_pages
    methods= GET
- **ger_car:**:
    filtra cada Car por su id
    retorna: el code, success y diccionario del carro
    methods= GET
- **search_car**:
    busqueda de los cars
    parámetros: URL(search y nitems)
    si detecta el search:
        retorna un format
    if body:
    parámetros: JSON(start_price string, end_price string, model string, brand string, year string)
    methods= POST
**========**

# Users_routes
**URL:**"/users"
- **register**:
    registra a los usuarios
    parámetros: JSON(username string, email string, password string)
    retorna: un mensaje que el usuario fue creado satisfactoriamente
    methods= POST
- **logged_in**:
    retorna: el usuario ya esta logeado 
    methods= GET
- **logout**:
    retorna: el usuario se desconectó con exito 
    methods= DELETE
- **login**:
    si el usuario esta identificado
    parámetro: JSON(email string, password string)
    si el usuario existe retorna: el usuario inició con exito
    methods= POST
- **get_profile_page**:
    parámetro: id del usuario (URL)
    retorna: Usuario encontrado 
    methods= GET
- **profile_page**:
    ...
- **inject_permissions**:
    retorna: un diccionario con sus permisos
- **permission_required**:
    ...
- **admin_required**:
    ...
- **inject_permissions**:
    ...
**==================================**
# ERRORS
# errors_handlers   
-**bad_request**:
    error 400, petición inválida
-**auth_required**:
    error 401, Se requiere autenticación
-**page_restricted**:
    error 403, Página restringida
-**page_not_found**:
    error 404, Página no encontrada
-**invalid_request**:
    error 412, Solicitud no válida
-**internal_server_error**:
    error 500, Error interno del servidor
-**handle_exception**:
    error 401, Se requiere autenticación

# FUNCIONES :
-**create_all_articles**: 
    crea todos los articulos
-**insert_roles**: 
    dentro de Role, ...

# CLASES:

+ Article:
    - columnas: id, title, description, content, image_url, author, date_published, category 
+ CARS:
    - columnas: id, name, image_url, price, model, category, year_production, mileage, transmission, engine_displacement, drivetrain, color, location.

+ Permission:
    COMMENT = 0x02
    WRITE_ARTICLES = 0x04
    MODERATE_COMMENTS = 0x08
    ADMINISTER = 0x80
+ Role:
    - crea los roles con las columnas: id, name, default, permissions
    - insert_roles():
    ...
+ User:
    - columnas: id, username, email, password_hash, image_url, role_id, posts, comments 

    ...
# Descripción:

new_ routes:
+ 

Nuestra aplicación es un sitio web el cual contiene:
+ Noticias relacionadas a los autos
+ Catalogo de diversas marcas de autos
+ Un foro donde permitirá a los usuarios compartir reviews y opiniones
+ Permite registrar a los usuarios en nuestra base de datos

# Objetivos principales / Misión / Visión
+ Objetivos principales:
    Nuestro objetivo como desarrolladores es facilitar la búsqueda de información
    sobre automóviles para los usuarios, como es en las noticias y precios de los
    autos usando un filtro que agilizará la búsqueda.
+ Misión:
    Cumplir los requerimientos del proyecto para tener una buena presentación a la
    hora de aplicar los métodos vistos en clase para la funcionalidad de la 
    aplicación
+ Visión:
    Queremos llegar a la mayor cantidad de usuarios y así ayudarlos en el proceso de 
    decisión de compra de el auto que más se acomode a sus necesidades

# Manejo de errores:

# Como ejecutar el sistema:


# Licencia



# Librerias utilizadas:
- 