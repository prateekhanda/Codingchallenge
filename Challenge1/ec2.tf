#Create EC2 Instance
resource "aws_instance" "webserver1" {
  ami                    = var.ami
  instance_type          = "t2.micro"
  availability_zone      = "us-east-1a"
  vpc_security_group_ids = [aws_security_group.webserver-sg.id]
  subnet_id              = aws_subnet.public-subnet-1.id
  user_data              = file("webserver.sh")

  tags = {
    Name = "Apache Web Server"
  }

}

resource "aws_instance" "webserver2" {
  ami                    = var.ami
  instance_type          = "t2.micro"
  availability_zone      = "us-east-1b"
  vpc_security_group_ids = [aws_security_group.webserver-sg.id]
  subnet_id              = aws_subnet.public-subnet-2.id
  user_data              = file("webserver.sh")

  tags = {
    Name = "Apache Web Server"
  }

}
