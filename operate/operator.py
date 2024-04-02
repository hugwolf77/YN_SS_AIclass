import torch
from torch import nn
from torch import optim

from sklearn.metrics import roc_auc_score

### VALIDATION FUNCTION
def validation(model, loader, criterion, device="cpu"):
    model.eval()
    loss = 0
    preds_all = torch.LongTensor()
    labels_all = torch.LongTensor()
    
    with torch.no_grad():
        for batch_x, labels in loader:
            labels_all = torch.cat((labels_all, labels), dim=0)
            batch_x, labels = batch_x.to(device), labels.to(device)
            labels = labels.unsqueeze(1).float()
            
            output = model.forward(batch_x)
            loss += criterion(output,labels).item()
            preds_all = torch.cat((preds_all, output.to("cpu")), dim=0)
    total_loss = loss/len(loader)
    auc_score = roc_auc_score(labels_all, preds_all)
    return total_loss, auc_score

### PREDICTION FUNCTION
def prediction(model, loader, device="cpu"):
    model.to(device)
    model.eval()
    preds_all = torch.LongTensor()
    
    with torch.no_grad():
        for batch_x in loader:
            batch_x = batch_x.to(device)
            
            output = model.forward(batch_x).to("cpu")
            preds_all = torch.cat((preds_all, output), dim=0)
    return preds_all


### TRAINING FUNCTION
def train_model(model, trainloader, validloader, criterion, optimizer, 
                scheduler, epochs=20, device="cpu", print_every=1):
    model.to(device)
    best_auc = 0
    best_epoch = 0
    for e in range(epochs):
        model.train()
        
        for batch_x, labels in trainloader:
            batch_x, labels = batch_x.to(device), labels.to(device)
            labels = labels.unsqueeze(1).float()
            
            # Training 
            optimizer.zero_grad()
            output = model.forward(batch_x)
            loss = criterion(output, labels)
            loss.backward()
            optimizer.step()
            scheduler.step()
            
        # at the end of each epoch calculate loss and auc score:
        model.eval()
        train_loss, train_auc = validation(model, trainloader, criterion, device)
        valid_loss, valid_auc = validation(model, validloader, criterion, device)
        if valid_auc > best_auc:
            best_auc = valid_auc
            best_epoch = e
            torch.save(model.state_dict(), "best-state.pt")
        if e % print_every == 0:
            to_print = "Epoch: "+str(e+1)+" of "+str(epochs)
            to_print += ".. Train Loss: {:.4f}".format(train_loss)
            to_print += ".. Valid Loss: {:.4f}".format(valid_loss)
            to_print += ".. Valid AUC: {:.3f}".format(valid_auc)
            print(to_print)
    # After Training:
    model.load_state_dict(torch.load("best-state.pt"))
    to_print = "\nTraining completed. Best state dict is loaded.\n"
    to_print += "Best Valid AUC is: {:.4f} after {} epochs".format(best_auc,best_epoch+1)
    print(to_print)
    return