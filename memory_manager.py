# Memory Manager


from database import load_memory, save_memory



def remember(text):

    memories = load_memory()

    memories.append(
        {
            "memory": text
        }
    )

    save_memory(memories)



def get_memories():

    return load_memory()
