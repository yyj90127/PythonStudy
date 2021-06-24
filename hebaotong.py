import pymongo
from  datetime import *

class hebaotong(object):
    def connect_MongoDB(self):
        client = pymongo.MongoClient("tech-tst-mongo.zhonganinfo.com", 27017)  # host：数据库所在的ip地址，port：端口号
        db = client.iyb_crm  # 连接要操作的数据库（数据库名：mydb）
        db.authenticate("iyb_crm_dev", "iyb_crm_dev_b47caf")  # 账号，密码
        return (client, db)

    def connect_db(self):
        collection_a = self.connect_MongoDB()[1].crm_underwrite_history
        collection_b = self.connect_MongoDB()[1].crm_underwrite_smallill_config
        collection_c = self.connect_MongoDB()[1].crm_underwrite_product_disease
        collection_d = self.connect_MongoDB()[1].crm_underwrite_product
        result_a = collection_a.aggregate([{"$match" : {"$and" : [{"gmtCreated" : {"$lte" : datetime.utcnow()}}, {"gmtCreated" : {"$gte" : datetime.utcnow() - timedelta(days=30)}},{"diseaseSid" : { "$ne" : None}},{"isDeleted" : "N"}]}}, {"$group" : {"_id" : "$diseaseSid", "count" : {"$sum" : 3}}}, {"$sort" : {"count" : -1}},{"$limit":20}])
        a = 1
        for i in result_a:
            j = []
            result_b = collection_b.find_one({"$and" :[{"sid" : i["_id"]}, {"isDeleted": "N"}]})
            if result_b is not None:
                result_c = collection_c.find({ "$and" : [{ "$and" : [{"name" : result_b["name"]}, {"isDeleted" : "N"}, {"risk" : { "$ne" : "H" }}] }, { "$or" : [{"riskConclusion.conclusion":"ACCEPT"}, {"riskConclusion.conclusion":"EXTRA"}, {"riskConclusion.conclusion":"EXCEPT"}, {"riskConclusion.conclusion":"POSTPONE"}, {"riskConclusion.conclusion":"EVALUATION"}] }] })
                b = 0
                for k in result_c:
                    result_d = collection_d.find_one({"$and" :[{"productId" : k["productId"]}, {"isDeleted": "N"}]})
                    if result_d is not None:
                        b = b+1
                if a <= 20:
                    j.append(a)
                    j.append(result_b["name"])
                    j.append(str(i["count"])+"人气")
                    j.append(str(b)+"产品")
                    print(j)
                    a = a+1


    def close_MongoDB(self):
        self.connect_MongoDB()[0].close()


if __name__ == '__main__':
    A = hebaotong()
    A.connect_db()
    A.close_MongoDB()