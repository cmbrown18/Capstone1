# This files contains all of the functions needed to modify the users.xml file
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element


def create_user():
    # Creates a user
    username = input("What is the new username: ")

    fullname = input("What is the user's full name: ")

    tree = ET.parse("users.xml")
    root = tree.getroot()

    username_xml = ET.SubElement(root, "username")
    fullname_xml = ET.SubElement(username_xml, "fullname")

    username_xml.text = username + "\n"
    fullname_xml.text = fullname + "\n"

    tree.write("users.xml")


def delete_user():
    # Deletes a user
    user = input("What user do you want to delete: ")

    tree = ET.parse("users.xml")
    root = tree.getroot()

    remove_list = list()

    for child in root.iter("username"):

        name = child.text

        if user in name:
            remove_list.append(child)

    for tag in remove_list:
        root.remove(tag)

    tree.write("users.xml")
