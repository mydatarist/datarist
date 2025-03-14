import sgMail from '@sendgrid/mail'

// Set the SendGrid API key
sgMail.setApiKey(process.env.SENDGRID_API_KEY)

export default function ContactForm() {
    // State for the form fields

    // State for the form status
    const [status, setStatus] = useState('')

    // Handle form submission
    const handleSubmit = async (formData) => {
        "user server"
        const rawFormData = {
            to: formData.get("email"),
            from: "your_sending_email",
            subject: `New message from ${formData.get("name")}`,
            text: formData.get("message"),
        }

        //Here need to write email sending functionality
        try {
            await sgMail.send(rawFormData)
            // Send a success response
            console.log("Email Send Successfully!")
        } catch (error) {
            // Send an error response
            console.log("Something went wrong, please try again!")
        }
    }

    return (
        <form action={handleSubmit}>
            <div>
                <label htmlFor="name">Name</label>
                <input
                    type="text"
                    id="name"
                    value={name}
                />
            </div>
            <div>
                <label htmlFor="email">Email</label>
                <input
                    type="email"
                    id="email"
                    value={email}
                />
            </div>
            <div>
                <label htmlFor="message">Message</label>
                <textarea
                    id="message"
                    value={message}
                />
            </div>
            <button type="submit">Send</button>
        </form>
    )
}