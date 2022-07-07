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
    se encarga de la paginación
    parametros: page(URL), entero
-**get_forum**:
    Se encarga de retornar todo el forum
-**create_post**:
    realiza los post de los forum
    parametros: JSON(post_body string, post_title string)
    retorna: retorna los posts y el total
-**delete_post**:
    Elimina el post
    parametros: JSON(post_id integer, post_body string y post_title string)
    retorna: el post_id eliminado y los restos 
-**update_post**:
    Sube el post
    parametros: JSON(post_id integer, post_body string y post_title string)
    retorna: el post_id y el total
-**get_post**:
    obtiene el post por el id (URL)
    parametros : id de post 
-**create_comment**:
    crea el comentario
    parametros: id de post (URL) ,JSON(comment_body string)
    retorna: el comentarios id y total de los comentarios
-**delete_comment**:
    Elimina el comentario
    parametros: id de post (URL), JSON(comment_id string)
    retorna: el comentarios id y total de los comentarios
-**update_comment**:
    Sube el comentario
    parametros: id de post (URL), JSON(comment_id integer, comment_body string)
    retorna: el comentarios id y total de los comentarios 


**========**
# HOME_routes:
-**Home_page**:
    selecciona aleatoriamente un carro y un articulo en un rango de 6
    ...
-**get_brands**:
    obtiene las marcas de los carros.
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
- **ger_car:**:
    filtra cada Car por su id
    retorna: el code, success y diccionario del carro
- **search_car**:
    busqueda de los cars
    parametros: URL(search y nitems)
    si detecta el search:
        retorna un format
    if body:
    parametros: JSON(start_price string, end_price string, model string, brand string, year string)
**========**

# Users_routes
**URL:**"/users"
- **register**:
    registra a los usuarios
    parametros: JSON(username string, email string, password string)
    retorna: un mensaje que el usuario fue creado satisfactoriamente
- **logged_in**:
    retorna: el usuario ya esta logeado 
- **logout**:
    retorna: el usuario se desconecto con exito
- **login**:
    si el usuario esta identificado
    parametro: JSON(email string, password string)
    si el usuario existe retorna: el usuario inicio con exito
- **get_profile_page**:
    parametro: id del usuario (URL)
    retorna: Usuario encontrado 
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
    para error 400, peticion invalida
-**auth_required**:
    para error 401, Se requiere autenticación
-**page_restricted**:
    para error 403, Página restringida
-**page_not_found**:
    para error 404, Página no encontrada
-**invalid_request**:
    para error 412, Solicitud no válida
-**internal_server_error**:
    para error 500, Error interno del servidor
-**handle_exception**:
    para error 401, Se requiere autenticación

# FUNCIONES :
-**create_all_articles**: 
        crea todos los articulos
-**insert_roles**: 
    dentro de Role, ...

# CLASES:

+ Article:
    - columnas: id, title, description, content, image_url, author, date_published, category 
    - get_new: retorna el total de news que exista
+ CARS
+ USERS
+ Permission:
    ...
+ Role:
    - crea los roles con las columnas: id, name, default, permissions
    -
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
    Nuestro objetivo como desarrolladores es facilitar la busqueda de informacion
    sobre automoviles para los usuarios, como es en las noticias y precios  de los
    carros usando un filtro que agilizara la busqueda.
+ Misión:
    Cumplir los requerimientos del proyecto para tener una buena presentacion a la
    hora de aplicar los metodos vistos en clase para la funcionalidad de la 
    aplicacion
+ Visión:
    Queremos llegar a la mayor cantidad de usuarios y asi ayudarlos en el proceso de 
    decisión de compra de el auto que más se acomode a sus necesidades

# Manejo de errores:

# Como ejecutar el sistema:


# Licencia



# Librerias utilizadas:
- 