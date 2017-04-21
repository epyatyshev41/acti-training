def getName(self):
    if self.vcard == None:
        self.vcard = self.storage.getVCardByEmailAddr(self.email)
    return self.vcard.getName()

def getTitle(self):
    if self.vcard == None:
        self.vcard = self.storage.getVCardByEmailAddr(self.email)
    return self.vcard.getTitle()
