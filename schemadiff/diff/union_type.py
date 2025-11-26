from schemadiff.changes.union import UnionMemberAdded, UnionMemberRemoved


class UnionType:
    def __init__(self, old_type, new_type) -> None:
        self.type = new_type
        self.old_values = old_type.types
        self.new_values = new_type.types

    def diff(self):
        changes = []

        old_values = {x.name for x in self.old_values}
        new_values = {x.name for x in self.new_values}

        added = new_values - old_values
        removed = old_values - new_values

        changes.extend(UnionMemberAdded(self.type, value) for value in added)
        changes.extend(UnionMemberRemoved(self.type, value) for value in removed)

        return changes
