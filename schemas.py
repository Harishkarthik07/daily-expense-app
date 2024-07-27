from app import ma
from models import User, Expense, ExpenseParticipant

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User

class ExpenseSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Expense
    participants = ma.Nested('ExpenseParticipantSchema', many=True)

class ExpenseParticipantSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ExpenseParticipant
