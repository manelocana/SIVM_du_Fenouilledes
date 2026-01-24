# SIVM du Fenouillèdes - Site Web

**Développeur :** Manel Ocaña 
**Projet :** Site web institutionnel pour le SIVM du Fenouillèdes, entreprise publique d'agents forestiers et de travaux avec machines agricoles.

---

## 1. Description

Ce projet est un site web institutionnel développé avec **Flask, HTML et CSS**.  

L'objectif principal est de fournir une **présentation claire** de l'entreprise, de ses activités, de ses services de machines agricoles, des agents forestiers, des actualités et d’un formulaire de contact.  

### Fonctionnalités principales :
- Page d'accueil (`Accueil`) avec hero/banner et présentation.  
- Sections **Maquinaria** et **Agents Forestiers**.  
- **Blog / Actualité** pour publier des nouvelles et communications.  
- **Formulaire de contact** avec email et localisation via **Google Maps**.  
- Design **responsive** : mobile-first et adaptable au desktop.  
- Préparé pour une future fonctionnalité de **login/admin** pour la gestion dynamique du contenu.  

---

## 2. Technologies

- **Backend :** Python 3.x, Flask  
- **Frontend :** HTML, CSS pur (sans frameworks externes, utilisation de classes utilitaires `.flex-column`, `.flex-center`)  
- **Intégrations :** Google Maps iframe pour la localisation  
- **Structure du projet :**  



          project/
          ├─ app/
          │ ├─ init.py
          │ ├─ routes/
          │ ├─ static/
          │ └─ templates/
          ├─ main.py
          ├─ requirements.txt
          └─ README.md

---

## 3. Prérequis

- Python 3.x  
- Flask  
- Les autres dépendances sont listées dans `requirements.txt`  

> ⚠ Les versions exactes seront vérifiées dans `requirements.txt` avant le déploiement.

---

## 4. Installation et exécution

  4.1 Cloner le projet :  
    
    git clone <URL-du-repository>
    cd <nom-du-projet>

  4.2. Activer l'environnement virtuel :

    source venv/bin/activate  # Linux / macOS
    venv\Scripts\activate     # Windows

  4.3. Installer les dépendances :

    pip install -r requirements.txt

  4.4. Lancer l'application :

    python main.py

  4.5. Ouvrir dans le navigateur :

    http://127.0.0.1:5000/

---

## 5. Structure des pages
- Accueil : Page principale avec hero, présentation et résumé des services.

- Maquinaria : Détails sur les machines et travaux réalisés.

- Agents Forestiers : Informations sur les agents et leurs missions.

- Actualité / Blog : Nouvelles et communiqués de l'entreprise.

- Contact : Formulaire de contact, adresse, téléphone, email et Google Maps intégré.

---

## 6. Améliorations futures

- Panel d’administration pour gérer les actualités et le contenu dynamique.

- Login pour utilisateurs/admin.

- Formulaire de contact avec envoi d’emails fonctionnel.

- Éventuelle intégration de petites animations CSS pour améliorer l’expérience utilisateur.

---

7. Auteur / Contact

    Développeur : Manel
     
    Email : manelocana.dev@gmail.com


