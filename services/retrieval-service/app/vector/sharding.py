class ShardManager:

    def __init__(self):
        self.shards = {}

    def add_shard(self, tenant_id, store):
        self.shards[tenant_id] = store

    def get(self, tenant_id):
        return self.shards.get(tenant_id)