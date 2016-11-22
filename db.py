#!/usr/bin/env python3.5
# -*- coding: UTF-8 -*-

try:
	from pymongo import MongoClient
except ImportError:
	raise ImportError('PyMongo is not installed')


class MongoDB(object):
	def __init__(self, host='localhost', port=27017, database_name=None, collection_name=None, drop_n_create=False):
		try:
			self._connection = MongoClient(host=host, port=port)
		except Exception as error:
			raise Exception(error)
		if drop_n_create:
			self.drop_db(database_name)
		self._database = None
		self._collection = None
		if database_name:
			self._database = self._connection[database_name]
		if collection_name:
			self._collection = self._database[collection_name]

	@staticmethod
	def check_state(obj):
		if not obj:
			return False
		else:
			return True

	def check_db(self):
		if not self.check_state(self._database):
			raise ValueError('Database is empty/not created')
	
	def check_collection(self):
		if not self.check_state(self._collection):
			raise ValueError('Collection is empty/not created')

	def get_overall_details(self):
		client = self._connection
		details = dict((db, [collection for collection in client[db].collection_names()])
					for db in client.database_names())
		return details
	
	def get_current_status(self):
		return {'connection': self._connection,
				'database': self._database,
				'collection': self._collection}

	def create_db(self, database_name=None):
		self._database = self._connection[database_name]

	def create_collection(self, collection_name=None):
		self.check_db()
		self._collection = self._database[collection_name]

	def get_database_names(self):
		return self._connection.database_names()

	def get_collection_names(self):
		self.check_collection()
		return self._database.collection_names(include_system_collections=False)

	def drop_db(self, database_name):
		self._database = None
		self._collection = None
		return self._connection.drop_database(str(database_name))

	def drop_collection(self):
		pass

	def insert(self, post):
		self.check_collection()
		post_id = self._collection.insert_one(post).inserted_id
		return post_id

	def insert_many(self):
		self.check_collection()
		pass

	def update(self):
		self.check_collection()
		pass

	def find(self):
		self.check_collection()
		pass

	def query(self):
		self.check_collection()
		pass
	
	def create_index(self):
		pass

