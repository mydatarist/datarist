import Script from "next/script";

<Script src={'https://www.googletagmanager.com/gtag/js?id=G-RS1PX7109Y'} strategy="afterInteractive" />
        <Script id="google-analytics" strategy="afterInteractive">
          {"window.dataLayer = window.dataLayer || []; function gtag(){dataLayer.push(arguments);}"}
        </Script>
        <Script src={`https://www.googletagmanager.com/gtag/js?id=G-RS1PX7109Y`} strategy="afterInteractive" />
          <Script id='google-analytics' strategy="afterInteractive"
                dangerouslySetInnerHTML={{
                    __html: `
                    window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-RS1PX7109Y');
                `,
                }}
            />