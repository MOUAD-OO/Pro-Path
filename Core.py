
import pandas as pd
import os
from sklearn.neighbors import KNeighborsClassifier
import smtplib
from email.mime.text import MIMEText


data=pd.read_excel("data_final1.xlsx")
data=data.drop(columns=['id_etudiant'])
X=data.drop(columns=['electif_1','electif_2','electif_3','Parcours_S8','option_3A','PFE','stage_2A','Filiere_3A','majeur','cesure'])
y=data.drop(columns=["stage1A", "centre d'interet",'note_mathématique', 'note_physique',
       'note_mécanique', 'note_informatique', 'note_sciencedentreprise',
       'note_sciencehumaine', 'note_adpl', 'note_lbd', 'note_langues'])


neigh = KNeighborsClassifier(n_neighbors=3)


new_X = pd.get_dummies(X)
new_y = pd.get_dummies(y)

new_X = new_X.apply(lambda col: col.astype(int) if col.dtype == bool else col)
new_y = new_y.apply(lambda col: col.astype(int) if col.dtype == bool else col)


col_x=new_X.columns

neigh.fit(new_X, new_y)



class Utilisateur:
    def __init__(self, nom, prenom, adresse, mot_de_passe):
        self.nom = nom
        self.prenom = prenom
        self.adresse = adresse
        self.mot_de_passe = mot_de_passe

class Apprenant(Utilisateur):
    def __init__(self, nom, prenom, adresse, mot_de_passe):
        super().__init__(nom, prenom, adresse, mot_de_passe)
        self.informations = {}

    




    def rc(self,results):

        predicted_y=neigh.predict([results])
        col=new_y.columns
        majeur=""
        electif_3=""
        electif_1=""
        electif_2=""
        stage_2A=""
        option_3A=""
        Filiere_3A=""
        Parcours_S8=""
        PFE=""
        cesure=""
        for i in range(len(col)) :
            if predicted_y[0][i]==1:
                key= col[i].split("_")[0]
                indx=col[i].split("_")[1]
                value=col[i].split("_")[-1]
                
                if key == "majeur":
                    majeur = value
                elif key == "electif" and indx=='1':
                    electif_1 = value
                elif key == "electif" and indx=='2':
                    electif_2 = value
                elif key == "electif" and indx=='3':
                    electif_3 = value
                elif key == "Parcours":
                    Parcours_S8 = value
                elif key == "stage":
                    stage_2A = value
                elif key == "cesure":
                    cesure = value
                elif key == "option":
                    option_3A = value
                elif key == "Filiere":
                    Filiere_3A = value
                elif key == "PFE":
                    PFE = value
        recommendation = "Vous pouvez suivre le majeur de {}, et les électifs ({},".format(majeur, electif_1)
        recommendation += " {}, {}), et choisir le parcours {}, effectuer un stage en {}, et opter pour Une césure {}, faire la filière {} et l'option {} avec un projet de fin d'études en {}.".format(electif_2, electif_3, Parcours_S8, stage_2A, cesure,Filiere_3A,option_3A, PFE)
        return recommendation
    
    
    
    
    

    def demande_de_rdv_specific_mentoring(self, demande):
        demande=[self.nom, self.prenom, self.adresse] + demande
        
        # Read existing requests
        try:
            with open('mentoring_request1.txt', 'r') as f:
                a = f.readlines()
        except FileNotFoundError:
            a = []
        
        # Append the new request
        a.append('\t'.join(demande) + '\n')
        
        # Write all requests back to the file
        with open('mentoring_request1.txt', 'w') as f:
            for e in a:
                f.write(e)
        
        pass







class Mentor(Utilisateur):
    def __init__(self, nom, prenom, adresse, mot_de_passe):
        super().__init__(nom, prenom, adresse, mot_de_passe)
        self.demandes_de_mentorat = []
    def consulter_demandes_mentorat(self):
        # Define the file path
        filename = "mentoring_request1.csv"


        # Load the file into a Pandas DataFrame
        df = pd.read_csv(filename, sep=',')  # Use sep='\t' if it's tab-separated

        # Convert DataFrame to a list of dictionaries
        requests = df.to_dict(orient='records')

        return requests
    

    def afficher_demandes_pour_mentor(self):
        toutes_les_demandes = self.consulter_demandes_mentorat()
        demandes_mentor = [demande for demande in toutes_les_demandes if demande["mentor"].lower() == self.nom.lower()]

        return demandes_mentor
    

class Professeur(Mentor):
    def __init__(self, nom, prenom, adresse, mot_de_passe):
        super().__init__(nom, prenom, adresse, mot_de_passe)


#this will be our upcomming feature where the student can check the curriculum of the school
#the administration should upload the pdf files of the curriculum
#the student can download the pdf files
class Scolarite:
    def __init__(self, folder_path="uploaded_files"):
        self.folder_path = folder_path
        self.ensure_directory_exists(folder_path)
        self.maquettes = self.load_files()

    def ensure_directory_exists(self, directory):
        if not os.path.exists(directory):
            os.makedirs(directory)

    def load_files(self):
        # Load existing PDF files from the folder
        return [os.path.join(self.folder_path, f) for f in os.listdir(self.folder_path) if f.endswith('.pdf')]

    def ajouter_maquette(self, uploaded_file):
        if uploaded_file is not None:
            chemin_pdf = os.path.join(self.folder_path, uploaded_file.name)
            if not os.path.exists(chemin_pdf):  # Check if file already exists to prevent duplicates
                with open(chemin_pdf, "wb") as f:
                    f.write(uploaded_file.getbuffer())
                self.maquettes.append(chemin_pdf)
                return f"Maquette PDF ajoutée: {chemin_pdf}"
            else:
                return "Cette maquette PDF est déjà ajoutée."
        else:
            return "Aucun fichier chargé."

    def afficher_maquettes(self):
        # Reload the files each time this method is called to ensure it's updated
        self.maquettes = self.load_files()
        return [(os.path.basename(fichier), fichier) for fichier in self.maquettes]


#this is the mail function that will be used to by mentors 

def send_email(recipient_email, subject, message):
    sender_email = "azrouamsh@gmail.com"  #Hello teaher this is my personnel email i trust you with it :D fell free to test it 
    password = "stnk jlyi xfkp qjnu"  # this is a password you from your email account

    # Set up the email
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient_email
    try:
        # Connect to the Gmail SMTP server
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, password)
            server.sendmail(sender_email, recipient_email, msg.as_string())
        print(f"Email sent successfully to {recipient_email}")
    except Exception as e:
        print(f"Failed to send email to {recipient_email}: {e}")

