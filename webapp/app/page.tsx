import { Button } from "@/components/ui/button"
import { Terminal, ArrowRight, Cloud, Command } from "lucide-react"
import Link from "next/link"
import Image from "next/image"
import { CopyButton } from "@/components/copy-button"

export default function Home() {
  return (
    <div className="flex min-h-screen flex-col">
      <header className="px-4 lg:px-6 h-19 flex items-center border-b">
        <Link className="flex items-center justify-center" href="#">
          <Image
            src="/rayzer.png"
            alt="Rayzer Logo"
            width={66}
            height={66}
            className="h-auto w-16"
          />
          <span className="ml-2 text-xl font-bold">Rayzer</span>
        </Link>
        <nav className="ml-auto flex gap-4 sm:gap-6">
          <Link className="text-sm font-medium hover:underline underline-offset-4" href="#">
            Features
          </Link>
          <Link className="text-sm font-medium hover:underline underline-offset-4" href="#">
            Documentation
          </Link>
          <Link className="text-sm font-medium hover:underline underline-offset-4" href="#">
            GitHub
          </Link>
        </nav>
      </header>
      <main className="flex-2">
        <section className="w-full py-0 md:py-2 lg:py-16 xl:py-48">
          <div className="container px-4 md:px-6 max-w-screen-xl mx-auto">
            <div className="flex flex-col items-center space-y-2 text-center">
              <div className="mb-4">
                <Image
                  src="/rayzer.png"
                  alt="Rayzer Logo"
                  width={10}
                  height={10}
                  className="h-40 w-auto"
                />
              </div>
              <div className="space-y-2">
                <h1 className="text-3xl font-bold tracking-tighter sm:text-4xl md:text-5xl lg:text-6xl/none">Rayzer</h1>
                <p className="text-xl md:text-2xl font-medium text-primary">Fastest way to get started with Ray</p>
                <p className="mx-auto max-w-[700px] text-muted-foreground md:text-xl mt-">
                  Start building your Ray applications in seconds.
                  {/* focus on your distributed applications. */}
                </p>
              </div>
              <div className="w-full max-w-3xl mx-auto mt-8 relative">
                <div className="bg-zinc-900 rounded-lg overflow-hidden border border-zinc-700">
                  <div className="flex items-center px-4 py-2 bg-zinc-800">
                    <Terminal className="h-4 w-4 text-zinc-400 mr-2" />
                    <span className="text-sm text-zinc-400">Terminal</span>
                  </div>
                  <div className="p-4 overflow-x-auto">
                    <pre className="text-sm md:text-base text-zinc-100 font-mono">
                      <code>curl -sSL https://raw.githubusercontent.com/robin-anyscale/rayzer/main/install.sh | bash -s --</code>
                    </pre>
                  </div>
                </div>
                <CopyButton text="curl -sSL https://raw.githubusercontent.com/robin-anyscale/rayzer/main/install.sh | bash -s --" className="absolute right-4 top-1/2 mt-2" />
              </div>
              <div className="flex flex-col sm:flex-row gap-4 mt-6">
                <Button className="gap-1">
                  Get Started <ArrowRight className="h-4 w-4" />
                </Button>
                <Button variant="outline">View Documentation</Button>
              </div>
            </div>
          </div>
        </section>
        <section className="w-full py-12 md:py-24 lg:py-32 bg-gray-50">
          <div className="container px-4 md:px-6 max-w-screen-xl mx-auto">
            <div className="flex flex-col items-center justify-center space-y-4 text-center">
              <div className="space-y-2">
                <h2 className="text-3xl font-bold tracking-tighter md:text-4xl">Why Rayzer?</h2>
                <p className="max-w-[700px] text-muted-foreground md:text-xl">
                  Rayzer makes Ray cluster management simple, fast, and reliable.
                </p>
              </div>
            </div>
            <div className="mx-auto grid max-w-5xl items-center gap-6 py-12 lg:grid-cols-3">
              <div className="flex flex-col items-center space-y-4 rounded-lg border p-6">
                <div className="rounded-full bg-primary/10 p-3">
                  <Image
                    src="/rayzer.png"
                    alt="Rayzer Logo"
                    width={24}
                    height={24}
                    className="h-6 w-auto"
                  />
                </div>
                <h3 className="text-xl font-bold">Lightning Fast</h3>
                <p className="text-center text-muted-foreground">
                  Launch a Ray cluster in seconds with a single command. No complex setup required.
                </p>
              </div>
              <div className="flex flex-col items-center space-y-4 rounded-lg border p-6">
                <div className="rounded-full bg-primary/10 p-3">
                  <Cloud className="h-6 w-6 text-primary" />
                </div>
                <h3 className="text-xl font-bold">Cloud Ready</h3>
                <p className="text-center text-muted-foreground">
                  Deploy to any cloud provider with built-in optimizations for each platform.
                </p>
              </div>
              <div className="flex flex-col items-center space-y-4 rounded-lg border p-6">
                <div className="rounded-full bg-primary/10 p-3">
                  <Command className="h-6 w-6 text-primary" />
                </div>
                <h3 className="text-xl font-bold">Powerful CLI</h3>
                <p className="text-center text-muted-foreground">
                  Intuitive command-line interface for managing your Ray clusters with ease.
                </p>
              </div>
            </div>
          </div>
        </section>
        <section className="w-full py-12 md:py-24 lg:py-32">
          <div className="container px-4 md:px-6 max-w-screen-xl mx-auto">
            <div className="grid gap-10 lg:grid-cols-2 lg:gap-16">
              <div className="space-y-4">
                <div className="inline-block rounded-lg bg-muted px-3 py-1 text-sm">How It Works</div>
                <h2 className="text-3xl font-bold tracking-tighter md:text-4xl">From Zero to Ray in Three Steps</h2>
                <ul className="grid gap-6">
                  <li className="flex items-start gap-4">
                    <div className="flex h-8 w-8 shrink-0 items-center justify-center rounded-full bg-primary text-primary-foreground">
                      1
                    </div>
                    <div className="space-y-1">
                      <h3 className="text-xl font-bold">Install Rayzer</h3>
                      <p className="text-muted-foreground">
                        Run our one-line installation command to get Rayzer on your system.
                      </p>
                    </div>
                  </li>
                  <li className="flex items-start gap-4">
                    <div className="flex h-8 w-8 shrink-0 items-center justify-center rounded-full bg-primary text-primary-foreground">
                      2
                    </div>
                    <div className="space-y-1">
                      <h3 className="text-xl font-bold">Configure Your Cluster</h3>
                      <p className="text-muted-foreground">
                        Use simple commands to define your cluster size and requirements.
                      </p>
                    </div>
                  </li>
                  <li className="flex items-start gap-4">
                    <div className="flex h-8 w-8 shrink-0 items-center justify-center rounded-full bg-primary text-primary-foreground">
                      3
                    </div>
                    <div className="space-y-1">
                      <h3 className="text-xl font-bold">Launch and Scale</h3>
                      <p className="text-muted-foreground">
                        Start your cluster and scale it up or down as needed with simple commands.
                      </p>
                    </div>
                  </li>
                </ul>
              </div>
              <div className="flex items-center justify-center">
                <div className="relative w-full max-w-md">
                  <div className="bg-zinc-900 rounded-lg overflow-hidden border border-zinc-700">
                    <div className="flex items-center px-4 py-2 bg-zinc-800">
                      <Terminal className="h-4 w-4 text-zinc-400 mr-2" />
                      <span className="text-sm text-zinc-400">Terminal</span>
                    </div>
                    <div className="p-4 overflow-x-auto">
                      <pre className="text-sm text-zinc-100 font-mono">
                        <code>
                          $ curl -sSL https://get.rayzer.dev | bash
                          <br />
                          Installing Rayzer...
                          <br />
                          Rayzer installed successfully!
                          <br />
                          <br />$ rayzer init
                          <br />
                          Initializing new Ray cluster configuration...
                          <br />
                          Configuration created at ~/.rayzer/config.yaml
                          <br />
                          <br />$ rayzer launch
                          <br />
                          Launching Ray cluster...
                          <br />✓ Head node ready
                          <br />✓ Worker nodes connected
                          <br />✓ Cluster is ready!
                          <br />
                          <br />
                          Ray dashboard available at: http://localhost:8265
                        </code>
                      </pre>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>
        <section className="w-full py-12 md:py-24 lg:py-32 bg-gray-50">
          <div className="container px-4 md:px-6 max-w-screen-xl mx-auto">
            <div className="flex flex-col items-center justify-center space-y-4 text-center">
              <div className="space-y-2">
                <h2 className="text-3xl font-bold tracking-tighter md:text-4xl">Ready to Get Started?</h2>
                <p className="max-w-[700px] text-muted-foreground md:text-xl">
                  Launch your first Ray cluster in seconds with Rayzer.
                </p>
              </div>
              <div className="w-full max-w-2xl mx-auto mt-8 relative">
                <div className="bg-zinc-900 rounded-lg overflow-hidden border border-zinc-700">
                  <div className="flex items-center justify-between px-4 py-2 bg-zinc-800">
                    <div className="flex items-center">
                      <Terminal className="h-4 w-4 text-zinc-400 mr-2" />
                      <span className="text-sm text-zinc-400">Install Rayzer</span>
                    </div>
                  </div>
                  <div className="p-4 overflow-x-auto">
                    <pre className="text-sm md:text-base text-zinc-100 font-mono">
                      <code>curl -sSL https://get.rayzer.dev | bash</code>
                    </pre>
                  </div>
                </div>
                <CopyButton text="curl -sSL https://get.rayzer.dev | bash" className="absolute right-4 top-1/2" />
              </div>
              <div className="flex flex-col sm:flex-row gap-4 mt-6">
                <Button className="gap-1">
                  Get Started <ArrowRight className="h-4 w-4" />
                </Button>
                <Button variant="outline">View Documentation</Button>
              </div>
            </div>
          </div>
        </section>
      </main>
      <footer className="flex flex-col gap-2 sm:flex-row py-6 w-full shrink-0 items-center px-4 md:px-6 border-t max-w-screen-xl mx-auto">
        <div className="flex items-center gap-2">
          <Image
            src="https://hebbkx1anhila5yf.public.blob.vercel-storage.com/rayzer-kM4Nhm6P8kw2NgfUs5UqPcs0oostJE.png"
            alt="Rayzer Logo"
            width={20}
            height={20}
            className="h-5 w-auto"
          />
          <p className="text-sm text-muted-foreground">© {new Date().getFullYear()} Rayzer. All rights reserved.</p>
        </div>
        <nav className="sm:ml-auto flex gap-4 sm:gap-6">
          <Link className="text-sm hover:underline underline-offset-4" href="#">
            Terms of Service
          </Link>
          <Link className="text-sm hover:underline underline-offset-4" href="#">
            Privacy
          </Link>
          <Link className="text-sm hover:underline underline-offset-4" href="#">
            Contact
          </Link>
        </nav>
      </footer>
    </div>
  )
}

