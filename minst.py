# 导入必要的库
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

# 设置参数
batch_size = 64  # 批大小
learning_rate = 0.001  # 学习率
num_epochs = 50  # 训练轮数

# 检查GPU可用性并设置 device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f'Using device: {device}')

# 数据预处理
transform = transforms.Compose([
    transforms.ToTensor(),  # 将图片转换为张量
    transforms.Normalize((0.5,), (0.5,))  # 对数据进行归一化处理
])

# 加载 MNIST 数据集
train_dataset = datasets.MNIST(root='./data', train=True, transform=transform, download=True)
test_dataset = datasets.MNIST(root='./data', train=False, transform=transform, download=True)

train_loader = DataLoader(dataset=train_dataset, batch_size=batch_size, shuffle=True)
test_loader = DataLoader(dataset=test_dataset, batch_size=batch_size, shuffle=False)

# 定义神经网络模型
class SimpleNN(nn.Module):
    def __init__(self):
        super(SimpleNN, self).__init__()
        self.fc1 = nn.Linear(28 * 28, 128)  # 输入层到隐藏层
        self.fc2 = nn.Linear(128, 64)        # 隐藏层到隐藏层
        self.fc3 = nn.Linear(64, 10)         # 隐藏层到输出层

    def forward(self, x):
        x = x.view(-1, 28 * 28)  # 展平输入
        x = torch.relu(self.fc1(x))  # 激活函数
        x = torch.relu(self.fc2(x))  # 激活函数
        x = self.fc3(x)  # 输出层
        return x

# 初始化模型、损失函数和优化器，并将模型移到GPU
model = SimpleNN().to(device)
criterion = nn.CrossEntropyLoss()  # 交叉熵损失
optimizer = optim.Adam(model.parameters(), lr=learning_rate)  # Adam优化器

# 训练模型
for epoch in range(num_epochs):
    model.train()  # 设置模型为训练模式
    running_loss = 0.0
    for data, target in train_loader:
        data, target = data.to(device), target.to(device)  # 将数据和目标移动到GPU
        optimizer.zero_grad()  # 清零梯度
        output = model(data)  # 向前传播
        loss = criterion(output, target)  # 计算损失
        loss.backward()  # 反向传播
        optimizer.step()  # 更新权重
        running_loss += loss.item()

    print(f"Epoch [{epoch+1}/{num_epochs}], Loss: {running_loss/len(train_loader):.4f}")

# 测试模型
model.eval()  # 设置模型为评估模式
correct = 0
total = 0
with torch.no_grad():  # 禁用梯度计算
    for data, target in test_loader:
        data, target = data.to(device), target.to(device)  # 将数据移动到GPU
        output = model(data)
        _, predicted = torch.max(output.data, 1)  # 取最大概率对应的类别
        total += target.size(0)  # 累计样本数
        correct += (predicted == target).sum().item()  # 计算正确预测的数量

print(f'Accuracy: {100 * correct / total:.2f}%')
