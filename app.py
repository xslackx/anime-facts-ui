import streamlit as st
import random
from get_fact import APIFacts

class AnimeFactsUI:
    def __init__(self) -> None:

        st.set_page_config("Facts Anime")

        self.AnimeAPI = APIFacts()
        self.availables = self.AnimeAPI.all_animes()

        st.sidebar.header("Animes", divider=True)
        self.search_box = st.sidebar.text_input("Search")
        st.container(border=False).button("Refresh", 
                                          on_click=self.refresh_body, 
                                          icon="🔄", type="primary")
        self.update_sidebar()
        self.choice_name = None

    def adjust_name(self, name: str):
        return name.replace("_", " ").capitalize()
        
    def update_sidebar(self):
        if self.availables["success"]:
            for disponibles in self.availables["data"]:
                st.sidebar.button(disponibles["anime_name"], 
                                  key=disponibles["anime_name"], 
                                  on_click=self.refresh_body,args=(disponibles["anime_name"], ))
                    
    def update_body_fact(self, header_anime: str, image_anime: str, 
                            caption: str, fact_header: str, fact_text: str):
            
        h_a = header_anime if header_anime is not None else "Hunter x Hunter"
        i_a = image_anime if image_anime is not None else "https://m.media-amazon.com/images/M/MV5BZjNmZDhkN2QtNDYyZC00YzJmLTg0ODUtN2FjNjhhMzE3ZmUxXkEyXkFqcGdeQXVyNjc2NjA5MTU@._V1_FMjpg_UX1000_.jpg"
        cap = caption if caption is not None else h_a
        f_h = fact_header if fact_header is not None else "Fact"
        f_t = fact_text if fact_text is not None else "Hina s hat imitates her emotions."
            
        header_anime = st.columns(1)
        header_anime[0].container(border=False).header(h_a)
        body_anime = st.columns(1)

        body_anime[0].container(border=True, height=500).image(i_a,
                    caption=cap, use_container_width=True)

        body_anime[0].container(border=True).text_area(
                f_h,
                f_t
            )

    def get_any(self, data):
        t_max = len(data)
        n  = random.randint(0, t_max)
        try:
            return data[n]
        except:
            if t_max > 0:
                return data[-1]

    def refresh_body(self, anime = None):
        
        choice = anime if anime is not None else self.get_any(self.availables['data'])["anime_name"]
        anime_data = self.AnimeAPI.by_name(choice)
        choice_fact = self.get_any(anime_data["data"])
        self.update_body_fact(self.adjust_name(choice),
                              anime_data["anime_img"],
                              None, None,
                              choice_fact["fact"])

    def Tuti(self, nome):
        st.toast(nome)

    def user_search(self):
        if self.search_box:
            if self.availables["success"]:
                for disponibles in self.availables["data"]:
                    if self.search_box == disponibles["anime_name"]:
                        self.Tuti("Fetching fact")
                        
                
AnimeFactsUI()