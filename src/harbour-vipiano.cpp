/*
 * Copyright © 2017, 2020 Andrew Penkrat
 *
 * This file is part of ViPiano.
 *
 * ViPiano is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * ViPiano is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with ViPiano.  If not, see <http://www.gnu.org/licenses/>.
 */

#include <sailfishapp.h>
#include <QtQuick>
#include "synthesizer.h"


int main(int argc, char *argv[])
{
    QGuiApplication *app(SailfishApp::application(argc, argv));
    QCoreApplication::setOrganizationName("harbour-vipiano");
    QCoreApplication::setApplicationName("harbour-vipiano");
    QQuickView *view(SailfishApp::createView());
    qmlRegisterType<SynthPreset>();
    Synthesizer *synth = new Synthesizer();
    view->rootContext()->setContextProperty("synthesizer", synth);
    view->setSource(SailfishApp::pathTo("qml/harbour-vipiano.qml"));
    view->show();
    return app->exec();
}
