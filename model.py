from sklearn.ensemble import RandomForestClassifier
          
def train_model(X, y):
    """Entraîne un modèle Random Forest"""
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)
    return model