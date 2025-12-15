from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pymysql
import uvicorn
import traceback

app = FastAPI()


db = pymysql.connect(
    host='localhost',
    user='root',
    password='12903478',
    db='online_cinema',
    cursorclass=pymysql.cursors.DictCursor
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



class Actor(BaseModel):
    name: str

class Movie(BaseModel):
    title: str
    release_year: int
    genre: str

class User(BaseModel):
    username: str
    email: str

class View(BaseModel):
    user_id: int
    movie_id: int
    view_date: str 
    rating: float = None  

class MovieActor(BaseModel):
    movie_id: int
    actor_id: int
    role_name: str = None  


@app.post("/actors")
async def create_actor(actor: Actor):
    try:
        with db.cursor() as cursor:
            sql = "INSERT INTO actors (name) VALUES (%s)"
            cursor.execute(sql, (actor.name,))
            db.commit()
        return {"message": "Actor added successfully"}
    except Exception as e:
        db.rollback()
        print(traceback.format_exc())
        return {"error": str(e)}

@app.get("/actors")
async def get_actors():
    try:
        with db.cursor() as cursor:
            cursor.execute("SELECT * FROM actors")
            return {"actors": cursor.fetchall()}
    except Exception as e:
        print(traceback.format_exc())
        return {"error": str(e)}

@app.put("/actors/{actor_id}")
async def update_actor(actor_id: int, actor: Actor):
    try:
        with db.cursor() as cursor:
            sql = "UPDATE actors SET name=%s WHERE actor_id=%s"
            cursor.execute(sql, (actor.name, actor_id))
            db.commit()
        return {"message": f"Actor {actor_id} updated successfully"}
    except Exception as e:
        db.rollback()
        print(traceback.format_exc())
        return {"error": str(e)}

@app.delete("/actors/{actor_id}")
async def delete_actor(actor_id: int):
    try:
        with db.cursor() as cursor:
            sql = "DELETE FROM actors WHERE actor_id=%s"
            cursor.execute(sql, (actor_id,))
            db.commit()
        return {"message": f"Actor {actor_id} deleted successfully"}
    except Exception as e:
        db.rollback()
        print(traceback.format_exc())
        return {"error": str(e)}


@app.post("/movies")
async def create_movie(movie: Movie):
    try:
        with db.cursor() as cursor:
            sql = "INSERT INTO movies (title, release_year, genre) VALUES (%s, %s, %s)"
            cursor.execute(sql, (movie.title, movie.release_year, movie.genre))
            db.commit()
        return {"message": "Movie added successfully"}
    except Exception as e:
        db.rollback()
        print(traceback.format_exc())
        return {"error": str(e)}

@app.get("/movies")
async def get_movies():
    try:
        with db.cursor() as cursor:
            cursor.execute("SELECT * FROM movies")
            return {"movies": cursor.fetchall()}
    except Exception as e:
        print(traceback.format_exc())
        return {"error": str(e)}

@app.put("/movies/{movie_id}")
async def update_movie(movie_id: int, movie: Movie):
    try:
        with db.cursor() as cursor:
            sql = "UPDATE movies SET title=%s, release_year=%s, genre=%s WHERE movie_id=%s"
            cursor.execute(sql, (movie.title, movie.release_year, movie.genre, movie_id))
            db.commit()
        return {"message": f"Movie {movie_id} updated successfully"}
    except Exception as e:
        db.rollback()
        print(traceback.format_exc())
        return {"error": str(e)}

@app.delete("/movies/{movie_id}")
async def delete_movie(movie_id: int):
    try:
        with db.cursor() as cursor:
            sql = "DELETE FROM movies WHERE movie_id=%s"
            cursor.execute(sql, (movie_id,))
            db.commit()
        return {"message": f"Movie {movie_id} deleted successfully"}
    except Exception as e:
        db.rollback()
        print(traceback.format_exc())
        return {"error": str(e)}


@app.post("/users")
async def create_user(user: User):
    try:
        with db.cursor() as cursor:
            sql = "INSERT INTO users (username, email) VALUES (%s, %s)"
            cursor.execute(sql, (user.username, user.email))
            db.commit()
        return {"message": "User added successfully"}
    except Exception as e:
        db.rollback()
        print(traceback.format_exc())
        return {"error": str(e)}

@app.get("/users")
async def get_users():
    try:
        with db.cursor() as cursor:
            cursor.execute("SELECT * FROM users")
            return {"users": cursor.fetchall()}
    except Exception as e:
        print(traceback.format_exc())
        return {"error": str(e)}

@app.put("/users/{user_id}")
async def update_user(user_id: int, user: User):
    try:
        with db.cursor() as cursor:
            sql = "UPDATE users SET username=%s, email=%s WHERE user_id=%s"
            cursor.execute(sql, (user.username, user.email, user_id))
            db.commit()
        return {"message": f"User {user_id} updated successfully"}
    except Exception as e:
        db.rollback()
        print(traceback.format_exc())
        return {"error": str(e)}

@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    try:
        with db.cursor() as cursor:
            sql = "DELETE FROM users WHERE user_id=%s"
            cursor.execute(sql, (user_id,))
            db.commit()
        return {"message": f"User {user_id} deleted successfully"}
    except Exception as e:
        db.rollback()
        print(traceback.format_exc())
        return {"error": str(e)}


@app.post("/views")
async def create_view(view: View):
    try:
        with db.cursor() as cursor:
            sql = "INSERT INTO views (user_id, movie_id, view_date, rating) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (view.user_id, view.movie_id, view.view_date, view.rating))
            db.commit()
        return {"message": "View added successfully"}
    except Exception as e:
        db.rollback()
        print(traceback.format_exc())
        return {"error": str(e)}

@app.get("/views")
async def get_views():
    try:
        with db.cursor() as cursor:
            cursor.execute("SELECT * FROM views")
            return {"views": cursor.fetchall()}
    except Exception as e:
        print(traceback.format_exc())
        return {"error": str(e)}

@app.put("/views/{view_id}")
async def update_view(view_id: int, view: View):
    try:
        with db.cursor() as cursor:
            sql = """
            UPDATE views 
            SET user_id=%s, movie_id=%s, view_date=%s, rating=%s 
            WHERE view_id=%s
            """
            cursor.execute(sql, (view.user_id, view.movie_id, view.view_date, view.rating, view_id))
            db.commit()
        return {"message": f"View {view_id} updated successfully"}
    except Exception as e:
        db.rollback()
        print(traceback.format_exc())
        return {"error": str(e)}

@app.delete("/views/{view_id}")
async def delete_view(view_id: int):
    try:
        with db.cursor() as cursor:
            sql = "DELETE FROM views WHERE view_id=%s"
            cursor.execute(sql, (view_id,))
            db.commit()
        return {"message": f"View {view_id} deleted successfully"}
    except Exception as e:
        db.rollback()
        print(traceback.format_exc())
        return {"error": str(e)}


@app.post("/movie_actors")
async def create_movie_actor(link: MovieActor):
    try:
        with db.cursor() as cursor:
            sql = "INSERT INTO movie_actors (movie_id, actor_id, role_name) VALUES (%s, %s, %s)"
            cursor.execute(sql, (link.movie_id, link.actor_id, link.role_name))
            db.commit()
        return {"message": "Movie-Actor link added successfully"}
    except Exception as e:
        db.rollback()
        print(traceback.format_exc())
        return {"error": str(e)}

@app.get("/movie_actors")
async def get_movie_actors():
    try:
        with db.cursor() as cursor:
            cursor.execute("SELECT * FROM movie_actors")
            return {"movie_actors": cursor.fetchall()}
    except Exception as e:
        print(traceback.format_exc())
        return {"error": str(e)}

@app.put("/movie_actors/{movie_id}/{actor_id}")
async def update_movie_actor(movie_id: int, actor_id: int, link: MovieActor):
    try:
        with db.cursor() as cursor:
            sql = """
            UPDATE movie_actors 
            SET movie_id=%s, actor_id=%s, role_name=%s 
            WHERE movie_id=%s AND actor_id=%s
            """
            cursor.execute(sql, (link.movie_id, link.actor_id, link.role_name, movie_id, actor_id))
            db.commit()
        return {"message": f"Movie-Actor link {movie_id}-{actor_id} updated successfully"}
    except Exception as e:
        db.rollback()
        print(traceback.format_exc())
        return {"error": str(e)}

@app.delete("/movie_actors/{movie_id}/{actor_id}")
async def delete_movie_actor(movie_id: int, actor_id: int):
    try:
        with db.cursor() as cursor:
            sql = "DELETE FROM movie_actors WHERE movie_id=%s AND actor_id=%s"
            cursor.execute(sql, (movie_id, actor_id))
            db.commit()
        return {"message": f"Link movie {movie_id} - actor {actor_id} deleted successfully"}
    except Exception as e:
        db.rollback()
        print(traceback.format_exc())
        return {"error": str(e)}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8002)
