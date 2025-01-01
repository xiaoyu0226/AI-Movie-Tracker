from langchain_openai import ChatOpenAI
from langchain.schema.output_parser import StrOutputParser
from langchain.prompts import ChatPromptTemplate

class App:
    def __init__(self, data):
        self.data = data
        self.llm = ChatOpenAI(model="gpt-4o")
        self.template = "Recommend 5 '{genre}' movies."
        self.prompt_template = ChatPromptTemplate.from_template(self.template)
        self.chain = self.prompt_template | self.llm | StrOutputParser()


    def get_movies(self, status):
        self.conn = self.data.getConnection()
        self.dataCursor = self.conn.cursor()
        self.dataCursor.execute("SELECT * FROM movies WHERE status=?", (status,))
        movies = self.dataCursor.fetchall()
        self.conn.close()
        return movies

    def add_movie(self, title, year=None, description='', status='to_watch', progress=0):
        self.conn = self.data.getConnection()
        self.dataCursor = self.conn.cursor()
        self.dataCursor.execute('''
            INSERT INTO movies (title, year, description, status, progress) 
            VALUES (?, ?, ?, ?, ?)
        ''', (title, year, description, status, progress))
        self.conn.commit()
        self.conn.close()


    def default(self):
        watched = self.get_movies("watched")
        to_watch = self.get_movies("to_watch")
        watching = self.get_movies("watching")
        return watched, to_watch, watching

    def movie_recommendation(self, genre):
        response = self.chain.invoke({"genre": genre})
        movies = self.parse_movie_text(response)
        return movies

    def parse_movie_text(self, text):
        movies = text.strip().split("\n\n")[1:]

        movie_list = []
        for movie in movies:
            if "**" not in movie:
                continue
            title_and_year = movie.split('**')[1]
            title = title_and_year.split('(')[0]
            year = title_and_year.split('(')[1].split(')')[0]
            
            description = movie.split('-')[1].strip()
            
            movie_dict = {
                "title": title,
                "year": int(year),
                "description": description
            }
            movie_list.append(movie_dict)

        return movie_list
