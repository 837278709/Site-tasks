'''
Created on Jul 11, 2018
'''
import asyncio
from celery import shared_task
import motor.motor_asyncio
import pymongo


async def get_mongo_doc(future):
    client = motor.motor_asyncio.AsyncIOMotorClient(
        'mongodb://localhost:27017')
    db = client.test_db
    collection = db.galnet_news
    cursor = collection.find()
    cursor.sort('_id', pymongo.DESCENDING).limit(1)
    async for document in cursor:
        future.set_result(document)


@shared_task
def set_blog_data():
    loop = asyncio.get_event_loop()
    future = asyncio.Future()
    tasks = [
        asyncio.ensure_future(get_mongo_doc(future)),
    ]
    tasks = asyncio.wait(tasks)
    try:
        loop.run_until_complete(tasks)
        print(future.result())
    except Exception:
        pass
    finally:
        loop.close()


if __name__ == '__main__':
    set_blog_data()
