SERVICE_NAME="telegram-bot"
echo "Installing $SERVICE_NAME"
cp "service.sh" "/etc/init.d/$SERVICE_NAME"
chmod +x /etc/init.d/$SERVICE_NAME