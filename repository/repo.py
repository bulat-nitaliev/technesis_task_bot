from sqlalchemy.orm import Session
from sqlalchemy import select, func
from schemas import SitesSchema
from core import Sites,Product
from core import get_db

class Repository:
    def __init__(self, db_session:Session):
        self.db_session:Session = db_session

    def add_sites(self, lst_site:list[SitesSchema]):
        with self.db_session as session:
            session.bulk_insert_mappings(Sites, lst_site)
            session.commit()
       
    
    def get_sites(self):
        res = select(Sites)
        with self.db_session as session:
            return session.execute(res).scalars().all()
        
        
    def get_avg_price_by_site(self):
        stmt = (
            select(
                Sites.title.label('site_title'),
                func.avg(Product.price).label('average_price')
            )
            .join(Sites, Sites.id == Product.sites_id)
            .group_by(Sites.title)
        )
        with self.db_session as session:
            result = session.execute(stmt).fetchall()
            return result
         
    
  

def get_repo()->Repository:
    db_session = get_db()
    return Repository(db_session)