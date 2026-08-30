class MetadataFilter:

    @staticmethod
    def apply(results, metadata):
        filtered = []

        for item in results:
            if all(
                item["doc"].metadata.get(k) == v
                for k, v in metadata.items()
            ):
                filtered.append(item)

        return filtered