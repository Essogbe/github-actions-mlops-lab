# 📘 Guide YAML pour GitHub Actions

## Qu'est-ce que YAML ?

YAML (YAML Ain't Markup Language) est un format de sérialisation de données lisible par l'humain. GitHub Actions utilise YAML pour définir les workflows.

## Règles de Base

### 1. Indentation
- **TOUJOURS utiliser des espaces** (jamais de tabulations)
- **2 espaces** par niveau d'indentation
- L'indentation définit la hiérarchie

```yaml
parent:
  enfant:
    petit_enfant: valeur
```

### 2. Structures de Données

#### Scalaires (valeurs simples)
```yaml
nom: "Alice"
age: 25
actif: true
score: 3.14
```

#### Listes (arrays)
```yaml
# Style 1: avec tirets
fruits:
  - pomme
  - banane
  - orange

# Style 2: inline
couleurs: [rouge, vert, bleu]
```

#### Dictionnaires (objets)
```yaml
personne:
  nom: Alice
  age: 25
  ville: Paris
```

### 3. Commentaires
```yaml
# Ceci est un commentaire
name: Mon Workflow  # Commentaire en fin de ligne
```

### 4. Chaînes de Caractères

```yaml
# Sans guillemets (simple)
message: Bonjour tout le monde

# Avec guillemets doubles (permet l'échappement)
message: "Ligne 1\nLigne 2"

# Avec guillemets simples (littéral)
message: 'Il a dit: "Bonjour"'

# Multi-lignes avec |
script: |
  echo "Ligne 1"
  echo "Ligne 2"
  echo "Ligne 3"

# Multi-lignes avec > (remplace les retours par des espaces)
description: >
  Ceci est une très longue description
  qui sera sur une seule ligne.
```

### 5. Valeurs Spéciales

```yaml
valeur_nulle: null
valeur_vide: ~
booleen_vrai: true
booleen_faux: false
```

## Structure d'un Workflow GitHub Actions

```yaml
# Nom du workflow (optionnel mais recommandé)
name: Mon Premier Workflow

# Déclencheur(s)
on: push

# Jobs à exécuter
jobs:
  nom-du-job:
    runs-on: ubuntu-latest
    steps:
      - name: Première étape
        run: echo "Hello"
```

## Pièges Courants à Éviter

### ❌ Erreur : Tabulations
```yaml
jobs:
	build:  # ❌ Utilise des tabulations
```

### ✅ Correct : Espaces
```yaml
jobs:
  build:  # ✅ Utilise des espaces
```

### ❌ Erreur : Indentation incorrecte
```yaml
jobs:
  build:
  runs-on: ubuntu-latest  # ❌ Mauvaise indentation
```

### ✅ Correct
```yaml
jobs:
  build:
    runs-on: ubuntu-latest  # ✅ Bonne indentation
```

### ❌ Erreur : Caractères spéciaux non échappés
```yaml
message: Il m'a dit: "Bonjour"  # ❌ Guillemets non échappés
```

### ✅ Correct
```yaml
message: "Il m'a dit: \"Bonjour\""  # ✅ Guillemets échappés
# ou
message: 'Il m''a dit: "Bonjour"'
```

## Validation YAML

### En ligne de commande (avec Python)
```bash
python -c "import yaml; yaml.safe_load(open('workflow.yml'))"
```

### Éditeurs recommandés
- **VS Code** avec extension "YAML" par Red Hat
- **PyCharm** (support natif)
- Validation en ligne : [yamllint.com](http://www.yamllint.com/)

## Syntaxe GitHub Actions Spécifique

### Variables d'environnement
```yaml
env:
  MA_VARIABLE: valeur
  PYTHON_VERSION: 3.9
```

### Expressions
```yaml
# Utilise la syntaxe ${{ }}
if: ${{ github.ref == 'refs/heads/main' }}
run: echo "Branch: ${{ github.ref }}"
```

### Secrets
```yaml
env:
  API_KEY: ${{ secrets.MA_CLE_API }}
```

## Résumé des Bonnes Pratiques

✅ **À FAIRE**
- Utiliser 2 espaces pour l'indentation
- Valider votre YAML avant de committer
- Ajouter des commentaires pour expliquer les sections complexes
- Utiliser des noms descriptifs pour les jobs et steps

❌ **À ÉVITER**
- Les tabulations
- L'indentation incohérente
- Les fichiers sans validation préalable
- Les noms génériques comme "job1", "step1"

---

**Prochaine étape** : Créer votre premier workflow GitHub Actions ! 🚀