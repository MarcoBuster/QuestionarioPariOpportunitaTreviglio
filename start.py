#
#   This file is a part of "Questionario Pari Opportunità Treviglio";
# 	Copyright (c) 2018 The project Authors and Contributors (see AUTHORS and CONTRIBUTORS).
# 	See LICENSE file for further details:
# 	https://github.com/MarcoBuster/QuestionarioPariOpportunitaTreviglio/blob/master/LICENSE
#

from src import main, config

if __name__ == "__main__":
    main.app.run(
        config.HOST,
        config.PORT,
        config.DEBUG,
    )
