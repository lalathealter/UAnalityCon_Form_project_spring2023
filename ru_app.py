from flask import Flask
from flask import request, redirect, render_template
from sqlalchemy import create_engine, MetaData, Table, Integer, Column, Text

app = Flask(__name__)

def safe_visitordata(datadict: dict):
    engine = create_engine('sqlite:///db/database.db')
    engine.connect()
    metadata = MetaData()
    if len(datadict) == 6:
        listeners = Table('listeners', metadata,
                      Column('l_id', Integer(), primary_key=True),
                      Column('l_surname', Text(), nullable=False),
                      Column('l_name', Text(), nullable=False),
                      Column('l_patronymic', Text(), nullable=False),
                      Column('l_email', Text(), nullable=False),
                      Column('l_workplace', Text(), nullable=False),
                      Column('l_position', Text(), nullable=False),
                      )
        metadata.create_all(engine)

        ins = listeners.insert().values(
            l_surname= str(datadict.get('lname_russian')).replace("[", "").replace("]", "").replace("'", ""),
            l_name=str(datadict.get('fname_russian')).replace("[", "").replace("]", "").replace("'", ""),
            l_patronymic=str(datadict.get('patronym_russian')).replace("[", "").replace("]", "").replace("'", ""),
            l_email=str(datadict.get('email')).replace("[", "").replace("]", "").replace("'", ""),
            l_workplace=str(datadict.get('place_of_work')).replace("[", "").replace("]", "").replace("'", ""),
            l_position=str(datadict.get('position')).replace("[", "").replace("]", "").replace("'", "")
        )
        conn = engine.connect()
        r = conn.execute(ins)
        conn.commit()
    else:
        participants = Table('participants', metadata,
                      Column('p_id', Integer(), primary_key=True),
                      Column('p_surname', Text(), nullable=False),
                      Column('p_name', Text(), nullable=False),
                      Column('p_patronymic', Text(), nullable=True),
                      Column('p_email', Text(), nullable=False),
                      Column('p_workplace', Text(), nullable=False),
                      Column('p_position', Text(), nullable=False),

                      Column('p_academicdegree', Text(), nullable=False),
                      Column('p_academictitle', Text(), nullable=False),
                      Column('p_phone', Text(), nullable=False),
                      Column('p_enname', Text(), nullable=False),
                      Column('p_ensurname', Text(), nullable=False),
                      Column('p_enworkplace', Text(), nullable=False),
                      Column('p_enposition', Text(), nullable=False),

                      Column('p_enacademicdegree', Text(), nullable=False),
                      Column('p_enacademictitle', Text(), nullable=False),
                      Column('p_title', Text(), nullable=False),
                      Column('p_entitle', Text(), nullable=False),
                      Column('p_coautorsinfo', Text(), nullable=True),
                      Column('p_theses', Text(), nullable=False),
                      Column('p_reporttype', Text(), nullable=False),
        )
        metadata.create_all(engine)
        ins = participants.insert().values(
            p_surname=str(datadict.get('lname_russian')).replace("[", "").replace("]", "").replace("'", ""),
            p_name=str(datadict.get('fname_russian')).replace("[", "").replace("]", "").replace("'", ""),
            p_patronymic=str(datadict.get('patronym_russian')).replace("[", "").replace("]", "").replace("'", ""),
            p_email=str(datadict.get('email')).replace("[", "").replace("]", "").replace("'", ""),
            p_workplace=str(datadict.get('place_of_work')).replace("[", "").replace("]", "").replace("'", ""),
            p_position=str(datadict.get('position')).replace("[", "").replace("]", "").replace("'", ""),

            p_academicdegree=str(datadict.get('acad_degree_russian')).replace("[", "").replace("]", "").replace("'", ""),
            p_academictitle=str(datadict.get('acad_rank_russian')).replace("[", "").replace("]", "").replace("'", ""),
            p_phone=str(datadict.get('phone_number')).replace("[", "").replace("]", "").replace("'", ""),
            p_enname=str(datadict.get('fname_english')).replace("[", "").replace("]", "").replace("'", ""),
            p_ensurname=str(datadict.get('lname_english')).replace("[", "").replace("]", "").replace("'", ""),
            p_enworkplace=str(datadict.get('place_of_work_english')).replace("[", "").replace("]", "").replace("'", ""),
            p_enposition=str(datadict.get('position_english')).replace("[", "").replace("]", "").replace("'", ""),

            p_enacademicdegree=str(datadict.get('acad_degree_english')).replace("[", "").replace("]", "").replace("'", ""),
            p_enacademictitle=str(datadict.get('acad_rank_english')).replace("[", "").replace("]", "").replace("'", ""),
            p_title=str(datadict.get('report_name_russian')).replace("[", "").replace("]", "").replace("'", ""),
            p_entitle=str(datadict.get('report_name_english')).replace("[", "").replace("]", "").replace("'", ""),
            p_coautorsinfo=str(datadict.get('coauthors_info')).replace("[", "").replace("]", "").replace("'", ""),
            p_theses=str(datadict.get('report_thesis')).replace("[", "").replace("]", "").replace("'", ""),
            p_reporttype=str(datadict.get('report_type')).replace("[", "").replace("]", "").replace("'", "")
        )
        conn = engine.connect()
        r = conn.execute(ins)
        conn.commit()

@app.route("/", methods=['GET', 'POST'])
def main_page():
    if request.method == "POST":
        data = (request.form.to_dict(flat=False))
        safe_visitordata(data)
        return render_template("ru_accept.html")
    else:
        return redirect("/form_for_participants")


@app.route("/form_for_participants")
def form_participants():
    return render_template("ru_form.html", is_for_participants=True)


@app.route("/form_for_attendees")
def form_attendees():
    return render_template("ru_form.html", is_for_participants=False)

if __name__ == "__main__":
    app.run()