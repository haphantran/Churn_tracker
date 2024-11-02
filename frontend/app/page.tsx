import Image from "next/image";

export default function Home() {
    return (
        <div className="grid grid-rows-[20px_1fr_20px] items-center justify-items-center min-h-screen p-8 pb-20 gap-16 sm:p-20 font-[family-name:var(--font-geist-sans)]">
            <main className="flex flex-col gap-8 row-start-2 items-center sm:items-start">
                <Image
                    className="dark:invert"
                    src="/images/logo.png" // Placeholder logo path
                    alt="Credit Cards Churning Tracker logo"
                    width={180}
                    height={38}
                    priority
                />
                <h1 className="text-2xl font-bold">Welcome to Credit Cards Churning Tracker</h1>
                <p className="text-center sm:text-left">
                    Track and manage your credit card churns efficiently.
                </p>
                <ol className="list-inside list-decimal text-sm text-center sm:text-left font-[family-name:var(--font-geist-mono)]">
                    <li className="mb-2">
                        Get started by adding your first credit card.
                    </li>
                    <li>Monitor your rewards and churn dates easily.</li>
                </ol>

                <div className="flex gap-4 items-center flex-col sm:flex-row">
                    <a
                        className="rounded-full border border-solid border-transparent transition-colors flex items-center justify-center bg-foreground text-background gap-2 hover:bg-[#383838] dark:hover:bg-[#ccc] text-sm sm:text-base h-10 sm:h-12 px-4 sm:px-5"
                        href="/credit-cards/new"
                    >
                        <Image
                            className="dark:invert"
                            src="/icons/add-icon.svg" // Placeholder add icon path
                            alt="Add card icon"
                            width={20}
                            height={20}
                        />
                        Add Card
                    </a>
                    <a
                        className="rounded-full border border-solid border-black/[.08] dark:border-white/[.145] transition-colors flex items-center justify-center hover:bg-[#f2f2f2] dark:hover:bg-[#1a1a1a] hover:border-transparent text-sm sm:text-base h-10 sm:h-12 px-4 sm:px-5 sm:min-w-44"
                        href="/view-cards"
                    >
                        View Cards
                    </a>
                </div>
            </main>
            <footer className="row-start-3 flex gap-6 flex-wrap items-center justify-center">
                <a
                    className="flex items-center gap-2 hover:underline hover:underline-offset-4"
                    href="/learn-more"
                >
                    <Image
                        aria-hidden
                        src="/icons/learn-icon.svg" // Placeholder learn icon path
                        alt="Learn icon"
                        width={16}
                        height={16}
                    />
                    Learn More
                </a>
                <a
                    className="flex items-center gap-2 hover:underline hover:underline-offset-4"
                    href="/examples"
                >
                    <Image
                        aria-hidden
                        src="/icons/examples-icon.svg" // Placeholder examples icon path
                        alt="Examples icon"
                        width={16}
                        height={16}
                    />
                    Examples
                </a>
                <a
                    className="flex items-center gap-2 hover:underline hover:underline-offset-4"
                    href="https://yourwebsite.com"
                    target="_blank"
                    rel="noopener noreferrer"
                >
                    <Image
                        aria-hidden
                        src="/icons/globe-icon.svg" // Placeholder globe icon path
                        alt="Globe icon"
                        width={16}
                        height={16}
                    />
                    Go to yourwebsite.com →
                </a>
            </footer>
        </div>
    );
}
