import sqlalchemy as sa
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Passport(Base):
    __tablename__ = "passports"

    id = sa.Column(sa.Integer, primary_key=True)
    first_name = sa.Column(sa.String(225), nullable=False)
    last_name = sa.Column(sa.String(225), nullable=False)
    father_name = sa.Column(sa.String(225), nullable=False)
    date_of_birth = sa.Column(sa.Date, nullable=False)
    place_of_birth = sa.Column(sa.String(225), nullable=False)
    date_of_issue = sa.Column(sa.Date, nullable=False)
    date_of_expiry = sa.Column(sa.Date, nullable=False)
    gender = sa.Column(sa.String(10), nullable=False)
    passport_number = sa.Column(sa.String(225), nullable=False, unique=True)
    picture = sa.Column(sa.String(225), nullable=False)

    visas = sa.orm.relationship("Visa")

    def __repr__(self):
        return f"<Passport(id={self.id}, first_name={self.first_name}, last_name={self.last_name}, father_name={self.father_name}, date_of_birth={self.date_of_birth}, place_of_birth={self.place_of_birth}, date_of_issue={self.date_of_issue}, date_of_expiry={self.date_of_expiry}, gender={self.gender}, passport_number={self.passport_number})>"


class Visa(Base):
    __tablename__ = "visas"

    id = sa.Column(sa.Integer, primary_key=True)
    destination = sa.Column(sa.String(225), nullable=False)
    date_of_issue = sa.Column(sa.Date, nullable=False)
    date_of_expiry = sa.Column(sa.Date, nullable=False)
    type_of_visa = sa.Column(sa.String(225), nullable=False)
    passport_id = sa.Column(sa.Integer, sa.ForeignKey("passports.id"), nullable=False)
    passport = sa.orm.relationship("Passport", overlaps="visas")

    def __repr__(self):
        return f"<Visa(id={self.id}, destination={self.destination}, date_of_issue={self.date_of_issue}, date_of_expiry={self.date_of_expiry}, type_of_visa={self.type_of_visa}, passport_id={self.passport_id})>"


class Officer(Base):
    __tablename__ = "officers"

    id = sa.Column(sa.Integer, primary_key=True)
    first_name = sa.Column(sa.String(225), nullable=False)
    last_name = sa.Column(sa.String(225), nullable=False)
    user_name = sa.Column(sa.String(225), nullable=False, unique=True)
    password = sa.Column(sa.String(225), nullable=False)

    def __repr__(self):
        return f"<Officer(id={self.id}, first_name={self.first_name}, last_name={self.last_name}, user_name={self.user_name}, password={self.password})>"

class DB:
    def __init__(self):
        db_url = (
            "mysql://arsavizi_ashar:FzdqbujHyZLXBD7@168.119.212.5:3306/arsavizi_ashar"
        )
        self.engine = sa.create_engine(db_url)
        sessionmaker = sa.orm.sessionmaker(bind=self.engine)
        self.session = sessionmaker()
        Base.metadata.create_all(self.engine)

    def create_passport(
        self,
        first_name,
        last_name,
        father_name,
        date_of_birth,
        place_of_birth,
        date_of_issue,
        date_of_expiry,
        gender,
        passport_number,
        picture,
    ):
        passport = Passport(
            first_name=first_name,
            last_name=last_name,
            father_name=father_name,
            date_of_birth=date_of_birth,
            place_of_birth=place_of_birth,
            date_of_issue=date_of_issue,
            date_of_expiry=date_of_expiry,
            gender=gender,
            passport_number=passport_number,
            picture=picture,
        )
        self.session.add(passport)
        self.session.commit()

    def get_passport(self, passport_number):
        passport = self.session.query(Passport).filter_by(passport_number=passport_number).first()
        return passport

    def get_all_passports(self):
        passports = self.session.query(Passport).all()
        return passports

    def update_passport(
        self,
        passport_number,
        first_name,
        last_name,
        father_name,
        date_of_birth,
        place_of_birth,
        date_of_issue,
        date_of_expiry,
        gender,
        picture
    ):
        passport = self.session.query(Passport).filter_by(passport_number=passport_number).first()
        passport.first_name = first_name
        passport.last_name = last_name
        passport.father_name = father_name
        passport.date_of_birth = date_of_birth
        passport.place_of_birth = place_of_birth
        passport.date_of_issue = date_of_issue
        passport.date_of_expiry = date_of_expiry
        passport.gender = gender
        passport.picture = picture

        self.session.commit()

    def delete_passport(self, passport_number):
        passport = self.session.query(Passport).filter_by(passport_number=passport_number).first()
        self.session.delete(passport)
        self.session.commit()


    def add_visa(self, destination, date_of_issue, date_of_expiry, type_of_visa, passport_number):
        passport = self.session.query(Passport).filter_by(passport_number=passport_number).first()
        if passport is None:
            return False
        visa = Visa(
            destination=destination,
            date_of_issue=date_of_issue,
            date_of_expiry=date_of_expiry,
            type_of_visa=type_of_visa,
            passport=passport,
        )
        self.session.add(visa)
        self.session.commit()

    def get_visa(self, passport_number):
        passport = self.session.query(Passport).filter_by(passport_number=passport_number).first()
        if passport is None:
            return False
        visas = self.session.query(Visa).filter_by(passport=passport).all()
        return visas

    def get_all_visas(self):
        visas = self.session.query(Visa).all()
        return visas

    def update_visa(self, id, destination, date_of_issue, date_of_expiry, type_of_visa):
        visa = self.session.query(Visa).filter_by(id=id).first()
        visa.destination = destination
        visa.date_of_issue = date_of_issue
        visa.date_of_expiry = date_of_expiry
        visa.type_of_visa = type_of_visa

        self.session.commit()

    def delete_visa(self, id):
        visa = self.session.query(Visa).filter_by(id=id).first()
        self.session.delete(visa)
        self.session.commit()


    def create_officer(self, first_name, last_name, user_name, password):
        officer = Officer(
            first_name=first_name,
            last_name=last_name,
            user_name=user_name,
            password=password
        )
        self.session.add(officer)
        self.session.commit()

    def get_officer(self, user_name):
        officer = self.session.query(Officer).filter_by(user_name=user_name).first()
        return officer

    def get_all_officers(self):
        officers = self.session.query(Officer).all()
        return officers

    def update_officer(self, user_name, first_name, last_name, password):
        officer = self.session.query(Officer).filter_by(user_name=user_name).first()
        officer.first_name = first_name
        officer.last_name = last_name
        officer.password = password

        self.session.commit()

    def delete_officer(self, user_name):
        officer = self.session.query(Officer).filter_by(user_name=user_name).first()
        self.session.delete(officer)
        self.session.commit()    
