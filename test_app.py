import contact
import footer

def test_contact():
    assert contact.contact() == "Page de contact"

def test_footer():
    assert footer.footer() == "Pied de page"
