"""
Update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- get_member: Should return a member from the self._members list
"""

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = [
            
        ]
        self.add_member({
            "first_name": "John",
            "age": 33,
            "lucky_numbers": [7, 13, 22]
        })

        self.add_member({
            "first_name": "Jane",
            "age": 35,
            "lucky_numbers": [10, 14, 3]
        })

        self.add_member({
            "first_name": "Jimmy",
            "age": 5,
            "lucky_numbers": [1]
        })

    # This method generates a unique incremental ID
    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, member):
        # generamor primero un ID
        member['id'] = self._generate_id()
        # generamos el apellido
        member['last_name'] = self.last_name
        #añadimos a la lista a el nuevo miembro
        self._members.append(member)
        #retornamos la lista de miembros
        return member

   

    def delete_member(self, id):
        largo1 = len(self._members)
        self._members = [m for m in self._members if m['id'] != id]
        largo2 = len(self._members)
        if largo1 == largo2 :
            return False
        else :
            return True
    def get_member(self, id):
        miembro = [m for m in self._members if m['id'] == id]
        return miembro[0]

    # This method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members

jackson_family = FamilyStructure("Jackson")

print(jackson_family)



