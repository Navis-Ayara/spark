from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from ..database.models import Spark

engine = create_engine("sqlite:///sparks_store.db")

Session = sessionmaker(bind=engine)

session = Session()

def create_spark(content: str, context: str) -> None:
    spark = Spark(
        content=content,
        context=context
    )

    session.add(spark)
    session.commit()

def get_sparks() -> list[Spark]:
    sparks = session.query(Spark).all()

    return sparks

def get_sparks_by_context(context: str) -> list[Spark]:
    sparks = session.query(Spark).filter_by(context=context).all()

    return sparks

def edit_spark(spark_id: int, content_edit: str) -> bool:
    spark = session.query(Spark).where(Spark.id == spark_id).first()

    if spark:
        spark.content = content_edit
        session.commit()

        return True
    return False

def delete_spark(spark_id: int) -> bool:
    spark = session.query(Spark).where(Spark.id == spark_id).first()

    if spark:
        session.delete(spark)
        session.commit()

        return True
    return False
    