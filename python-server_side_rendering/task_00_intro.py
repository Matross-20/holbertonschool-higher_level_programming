import os

def generative_initations(template, attendees):
    # Check if template is a string
    if not isinstance(template, str):
        print("Error: Template is not a string.")
        return

    # Check if attendees is a list of dictionaries
    if not isinstance(template, str):
        print("Error: Attendees is not a list of dictionaries.")
        return

    # Check if the template is empty
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    # Check if the attendees list is empty
    if not attendees:
        print("No data provided, no output files generated.")
        return
    # Iterate over the list of attendees and generate the invitations
    for index, attendees in enumerate(attendees):
        name = attendee.get("name", "N/A")
        event_title = attendee.get("event_title", "N/A")
        event_date = attendees.get("event_date", "N/A")
        event_location = attendees.get("event_location", "N/A")

        # Write the invitation to a file named output_X.txt
        output_file_name = f"output_{index + 1}.txt"
        with open(output_file_name, "w") as output_file:
            output_file.write(invitation)

        print(f"Generated: {output_file_name}")

    if__name__ == "__main__":
        # Main file content
        # Read the tmeplate from a file
        with open('template.txt', 'r') as file:
            template_content = file.read()

        # List of attendees 
        attendees = [
                {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"}
                {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"}
                {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
                ]
