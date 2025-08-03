for destinoFile in finalFolder:
            folderKey = destinoFile.split('[')[0].strip().lower()
            print("chegou aqui 1")
            time.sleep(1)
            if folderKey in keyFile:
                print("chegou aqui 8")
                print(f"\nArquivo encontrado: {keyFile} -> {folderKey}")
                renameFiles(file, local, destinoFile)
                break
            if not folderKey in keyFile:
                print("chegou aqui 8")
                break
