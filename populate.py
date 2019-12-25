import psycopg2
import os
 
def populate():
    """ create tables in the PostgreSQL database"""
    questions = [
        "Name something your ex should have done sexually", 
        "Name the person here that Person A should hook up with",
        "Describe your first time in detail",
        "What is the sex skill you are most proud of?",
        "What is the messiest thing you have ever done sexually?",
        "Who do you think has had more sexual partners between person A and B?",
        "What is your most complimented anatomical feature?",
        "If we were in a porn together, what genre would it be?",
        "If we were trapped on a desert island, would we become lovers?",
        "How many sexual partners have you had?",
        "Show your tinder profile allow them to  suggest changes - if not, create one",
        "What is your partners best asset physically?",
        "When was the last time you masturbated?",
        "What is the other persons best physical feature?",
        "Sit on my lap and stare into my eyes intimately for 1 minute.",
        "How would you rate your oral sex skills out of ten?",
        "Have you been in love before and if so why didn’t it work out?",
        "What sounds do you make when you are having sex and can you make them?",
        "Which one of us is more attractive?", 
        "What music do you like to bang to?", 
        "Do you want kids if so how many?", 
        "Ideally how often should a couple have sex?", 
        "What’s the worst thing you did in your last relationship?",  
        "Have you ever cheated on anyone?", 
        "Have you ever had a sex dream about a celebrity?",
        "What was the last drug you took and when?", 
        "My favorite genre of porn is?", 
        "3 reasons someone should not date you",
        "What is your type?",
        "Do you like dirty talk/talk dirty to me",
        "What is something you are really insecure about", 
        "Would you say that you are 100 percent heterosexual",
        "What was your last breakup like? Have you completely healed from it?",
        "What makes for a good relationship",
        "On the count of three, both people say how many times that they masturbate in a week",
        "What is the biggest secret you have ever kept from someone",
        "If you had to eat one part of my body what would it be",
        "What would it take for us to have sex",
        "Finish the line for me “im most scared of…”",
        "If someone offered you one million dollars to never talk to me again would you",
        "Describe me to someone who’s never met me",
        "What is something you would want to change about me", 
        "Have you ever caught me having sex or masturbating",
        "Have i ever told you a secret  that you passed on to someone else/what is a fact that no one else knows about me",
        "what do think got you into harvard?",
        "What world do you go to when you daydream?",
        "Have two people guess each others kink and give reasoning"
    ]

    conn = None

    try:
        DATABASE_URL = os.environ['DATABASE_URL']
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        cur = conn.cursor()

        # sql = """ INSERT INTO questions (question) VALUES (%s)"""

        for q in questions:
            cur.execute(f" INSERT INTO questions (question) VALUES {q}", )

        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == "__main__":
    populate()