# AnalisisDeDatos31
# mi primer edicion de codigo

- Comandos Git
    -   Clonar un repositorio: git clone ruta_repositorio
    -   Actualizacion de mis cambios: git status 
    -   Agregar cambios: git add . (indicar los archivos modificados)
    -   Crear un commit: git commit -m "Comentario"
    -   Crear el push : git push origin main
    -   jalar los cambios: git pull origin main

- Comando Docker:
    Docker 1: 
        - Crear imagen: docker build --no-cache  -t image-test .
        - listar iamgenes: docker images
        - eliminar imagen: docker rmi -f id_imagen
        - ejecutar una imagen(contenedor): docker run -d -p 8000:8888 --name jupyter image-test
        - ver log de un contenedor: docker logs -f jupyter
        - eliminar un contenedor : docker rm -f nombre_contenedor