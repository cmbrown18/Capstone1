# This files contains all of the functions needed to modify the users.xml file
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element


def create_user():
    # Creates a user
    username = input("What is the new username: ")

    fullname = input("What is the user's full name: ")

    tree = ET.parse("Database/users.xml")
    root = tree.getroot()

    username_xml = ET.SubElement(root, "username")
    fullname_xml = ET.SubElement(username_xml, "fullname")

    username_xml.text = username + "\n"
    fullname_xml.text = fullname + "\n"

    tree.write("Database/users.xml")

def delete():
    # Deletes a user
    user = input("What user do you want to delete: ")

