import pdffunctions

import PySimpleGUI as genpdf


genpdf.theme("Light Blue 5")

label = genpdf.Text("Welcome to NoteCluster, you own personal note-maker")
welcome_label = genpdf.Text("Let's start making notes")
label2 = genpdf.Text("What's the name of the topic?")
input_box = genpdf.InputText(tooltip="Enter the topic", key="heading")
select_button = genpdf.Button("Select", size=10, image_source="", mouseover_colors="LightBlue2",
                              tooltip="Select topic name", key="Select")

generate_button = genpdf.Button("", size=15, image_source="pdf-icon.png",  mouseover_colors="LightBlue2",
                                key="GenPDF")
exit_button = genpdf.Button("Exit", size=10)

col1 = genpdf.Column([[label2, input_box]])
col2 = genpdf.Column([[select_button], [exit_button]])

layout = [[label], [welcome_label], [col1, col2], [generate_button]]

window = genpdf.Window("NoteCluster", layout=layout, font=("Helvetica", 18))
while True:
    event, values = window.read(timeout=100)

    match event:

      case genpdf.WIN_CLOSED:
            exit()

      case "Select":
          topic = values["heading"]
          main


     #   case "Edit":
     #       try:

          #  except IndexError:
         #       genpdf.popup("Please select an item first!", font=("Helvetica", 17), title="Error!")

      # case "GenPDF":


      case "Exit":
            exit()
     #   case "to-dos":
          #  window["to-do"].update(value=values['to-dos'][0])

window.close()
