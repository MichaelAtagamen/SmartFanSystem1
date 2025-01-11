from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.callbacks import SubscribeCallback

# Step 1: PubNub Configuration
pnconfig = PNConfiguration()
pnconfig.publish_key = "publish_key"    # Replace with your PubNub Publish Key
pnconfig.subscribe_key = "subscribe_key"  # Replace with your PubNub Subscribe Key
pnconfig.uuid = "uuid"  # Unique identifier for this client

# Step 2: Initialize PubNub
pubnub = PubNub(pnconfig)

# Step 3: Define a Callback to Handle Incoming Messages
class MySubscribeCallback(SubscribeCallback):
    def message(self, pubnub, message):
        print(f"Received message: {message.message}")

# Step 4: Add the Callback to PubNub
pubnub.add_listener(MySubscribeCallback())

# Step 5: Subscribe to a Channel
pubnub.subscribe().channels("michael_pi_channel").execute()

# Step 6: Publish a Test Message
def publish_message():
    pubnub.publish().channel("michael_pi_channel").message({"msg": "Hello, PubNub!"}).pn_async(
        lambda result, status: print("Message Published!" if not status.is_error() else f"Error: {status.error}")
    )

# Publish a test message
publish_message()

# Print to confirm script runs
print("PubNub script executed successfully. Waiting for messages...")
