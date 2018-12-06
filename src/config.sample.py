#
#   This file is a part of "Questionario Pari Opportunità Treviglio";
# 	Copyright (c) 2018 The project Authors and Contributors (see AUTHORS and CONTRIBUTORS).
# 	See LICENSE file for further details:
# 	https://github.com/MarcoBuster/QuestionarioPariOpportunitaTreviglio/blob/master/LICENSE
#

# -- Flask configuration --
HOST = ''
PORT = 0
DEBUG = True

# -- Database --
DATABASE_FILE = "master.db"
GOOGLE_CLIENT_ID = ""
DATABASE_TABLE = (
    """
    CREATE TABLE IF NOT EXISTS users (
                                        id TEXT PRIMARY KEY NOT NULL,
                                        first_name TEXT NOT NULL,
                                        last_name TEXT NOT NULL,
                                        mail TEXT
    );

    CREATE TABLE IF NOT EXISTS answers (
                                        q1 TEXT NOT NULL,
                                        q1A_1 TEXT,
                                        q1B_1 TEXT,
                                        q1B_2 TEXT,
                                        q2 TEXT NOT NULL,
                                        q3_io TEXT,
                                        q3_madre TEXT,
                                        q3_padre TEXT,
                                        q4 TEXT,
                                        q5 TEXT NOT NULL,
                                        q6_primo TEXT,
                                        q6_secondo TEXT,
                                        q6_terzo TEXT,
                                        q7_parita INTEGER NOT NULL,
                                        q7_disabilita INTEGER NOT NULL,
                                        q7_lavoro INTEGER NOT NULL,
                                        q7_istruzione INTEGER NOT NULL,
                                        q7_orientamento_sessuale INTEGER NOT NULL,
                                        q7_risorse_economiche INTEGER NOT NULL,
                                        q8_parita INTEGER NOT NULL,
                                        q8_disabilita INTEGER NOT NULL,
                                        q8_lavoro INTEGER NOT NULL,
                                        q8_istruzione INTEGER NOT NULL,
                                        q8_orientamento_sessuale INTEGER NOT NULL,
                                        q8_risorse_economiche INTEGER NOT NULL,
                                        q9_parita INTEGER NOT NULL,
                                        q9_disabilita INTEGER NOT NULL,
                                        q9_lavoro INTEGER NOT NULL,
                                        q9_istruzione INTEGER NOT NULL,
                                        q9_orientamento_sessuale INTEGER NOT NULL,
                                        q9_risorse_economiche INTEGER NOT NULL,
                                        q10_parita TEXT NOT NULL,
                                        q10_disabilita TEXT NOT NULL,
                                        q10_lavoro TEXT NOT NULL,
                                        q10_istruzione TEXT NOT NULL,
                                        q10_orientamento_sessuale TEXT NOT NULL,
                                        q10_risorse_economiche TEXT NOT NULL,
                                        q11 TEXT NOT NULL
    );
    """
)

# -- Misc --
FIELDS = (
    'q1',
    'q1A_1',
    'q1B_1', 'q1B_2',
    'q2',
    'q3_io', 'q3_madre', 'q3_padre',
    'q4',
    'q5',
    'q6_parita', 'q6_disabilita', 'q6_lavoro', 'q6_istruzione', 'q6_orientamento-sessuale', 'q6_risorse-economiche',
    'q7_parita', 'q7_disabilita', 'q7_lavoro', 'q7_istruzione', 'q7_orientamento-sessuale', 'q7_risorse-economiche',
    'q8_parita', 'q8_disabilita', 'q8_lavoro', 'q8_istruzione', 'q8_orientamento-sessuale', 'q8_risorse-economiche',
    'q9_parita', 'q9_disabilita', 'q9_lavoro', 'q9_istruzione', 'q9_orientamento-sessuale', 'q9_risorse-economiche',
    'q10_parita', 'q10_disabilita', 'q10_lavoro', 'q10_istruzione', 'q10_orientamento-sessuale',
    'q10_risorse-economiche',
    'q11'
)
