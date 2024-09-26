from app import create_app, db

app = create_app()

#Database initialization function
def create_db():
    with app.app_context():
        db.create_all()

if __name__=='__main__':
    create_db #call this once to ceate the databse tables
    app.run(debug=True)